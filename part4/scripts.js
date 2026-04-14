const BASE = 'http://127.0.0.1:5000/api/v1';

function getCookie(name) {
    for (let c of document.cookie.split(';')) {
        const [k, v] = c.trim().split('=');
        if (k === name) return v;
    }
    return null;
}

function getParam(key) {
    return new URLSearchParams(window.location.search).get(key);
}

function syncLoginLink() {
    const link = document.getElementById('login-link');
    if (link) link.style.display = getCookie('token') ? 'none' : 'block';
}

document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');
    syncLoginLink();

    // login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const pass = document.getElementById('password').value;

            const res = await fetch(`${BASE}/user/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password: pass })
            });

            if (res.ok) {
                const data = await res.json();
                document.cookie = `token=${data.access_token}; path=/`;
                window.location.href = 'index.html';
            } else {
                document.getElementById('error-message').textContent = 'Wrong email or password.';
            }
        });
    }

    // index - load places
    const placesList = document.getElementById('places-list');
    if (placesList) {
        fetch(`${BASE}/place/`, {
            headers: token ? { 'Authorization': token } : {}
        })
        .then(r => r.json())
        .then(places => {
            if (!places.length) {
                placesList.innerHTML = '<p>No places found.</p>';
                return;
            }
            places.forEach(p => {
                const card = document.createElement('div');
                card.className = 'place-card';
                card.dataset.price = p.price;
                card.innerHTML = `
                    <h3>${p.title}</h3>
                    <p class="price">$${p.price} / night</p>
                    <a href="place.html?id=${p.id}" class="details-button">View Details</a>
                `;
                placesList.appendChild(card);
            });
        })
        .catch(() => placesList.innerHTML = '<p>Could not load places.</p>');

        document.getElementById('price-filter')?.addEventListener('change', (e) => {
            const max = e.target.value;
            document.querySelectorAll('.place-card').forEach(card => {
                const show = max === 'all' || parseFloat(card.dataset.price) <= parseFloat(max);
                card.style.display = show ? 'block' : 'none';
            });
        });
    }

    // place details
    const detailsSection = document.getElementById('place-details');
    if (detailsSection) {
        const pid = getParam('id');
        if (!pid) { detailsSection.innerHTML = '<p>No place selected.</p>'; return; }

        fetch(`${BASE}/place/${pid}`, {
            headers: token ? { 'Authorization': token } : {}
        })
        .then(r => r.json())
        .then(place => {
            detailsSection.innerHTML = `
                <div class="place-info">
                    <h1>${place.title}</h1>
                    <p class="host">Host: ${place.owner_id}</p>
                    <p class="price">$${place.price} / night</p>
                    <p class="description">${place.description || ''}</p>
                </div>
            `;

            const reviewsList = document.getElementById('reviews-list');
            if (reviewsList) {
                if (place.reviews?.length) {
                    place.reviews.forEach(id => {
                        const card = document.createElement('div');
                        card.className = 'review-card';
                        card.innerHTML = `<p class="comment">Review: ${id}</p>`;
                        reviewsList.appendChild(card);
                    });
                } else {
                    reviewsList.innerHTML = '<p>No reviews yet.</p>';
                }
            }

            const addReview = document.getElementById('add-review');
            if (addReview) {
                addReview.style.display = token ? 'block' : 'none';
                document.getElementById('add-review-link').href = `add_review.html?id=${pid}`;
            }
        })
        .catch(() => detailsSection.innerHTML = '<p>Could not load place.</p>');
    }

    // add review
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        if (!token) { window.location.href = 'index.html'; return; }

        const pid = getParam('id');
        if (!pid) { window.location.href = 'index.html'; return; }

        reviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const text = document.getElementById('review-text').value;
            const rating = document.getElementById('rating').value;

            const res = await fetch(`${BASE}/review/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': token
                },
                body: JSON.stringify({ text, rating: parseInt(rating), place_id: pid })
            });

            if (res.ok) {
                alert('Review submitted!');
                reviewForm.reset();
            } else {
                document.getElementById('error-message').textContent = 'Could not submit review.';
            }
        });
    }
});

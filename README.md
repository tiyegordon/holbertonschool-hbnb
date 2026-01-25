Objective

I created a high-level package diagram that illustrates the three-layer architecture of the HBnB application and how these layers communicate through the Facade pattern. This diagram gives a clear conceptual overview of how the application is organized and how responsibilities are separated across layers.

Description

In this task, I developed a package diagram that visually represents HBnB’s structure across three main layers:

Presentation Layer (Services, API): I use this layer to handle user interaction with the application. It contains the services and API endpoints exposed to clients.

Business Logic Layer (Models): I keep the core business rules here, along with the domain models that represent system entities such as User, Place, Review, and Amenity.

Persistence Layer: I use this layer to abstract data storage and retrieval through repositories (data access components) that communicate with the database.

My diagram clearly shows these three layers, the components inside each one, and the communication flow between them. I represent the Facade pattern as the unified interface that the Presentation Layer uses to access Business Logic, helping keep the system modular and clean.

Steps I Followed
1. I reviewed layered architecture

I refreshed my understanding of layered architecture and confirmed how each layer should function in HBnB, making sure responsibilities stay separated and dependencies flow downward.

2. I studied the Facade pattern

I reviewed how the facade design pattern simplifies communication between layers by providing a single, clean interface instead of exposing internal complexity.

3. I identified the key components per layer

I mapped the core parts of the system into the correct layers:

Presentation Layer: API endpoints and service-level handlers

Business Logic Layer: Domain models (User, Place, Review, Amenity) and the application facade

Persistence Layer: Repositories / data access objects for each domain entity

4. I drafted the package diagram

I created a draft diagram that:

Separates the system into the three layers

Places the Application Facade in the Business Logic layer

Shows how the Presentation Layer communicates with Business Logic through the facade

Shows how Business Logic interacts with the Persistence layer via repositories

5. I reviewed and refined the diagram

I verified that the final diagram is:

Accurate to the HBnB architecture goal

Clean and easy to follow

Consistent with high-level package diagram expectations (layers, packages, and dependencies)

graph TD

subgraph Presentation_Layer
    API[API / Services]
end

subgraph Business_Logic_Layer
    FACADE[HBnB Facade]
    USER[User]
    PLACE[Place]
    REVIEW[Review]
    AMENITY[Amenity]
end

subgraph Persistence_Layer
    REPO[Repository / DAO]
    DB[(Database)]
end

API --> FACADE
FACADE --> USER
FACADE --> PLACE
FACADE --> REVIEW
FACADE --> AMENITY

USER --> REPO
PLACE --> REPO
REVIEW --> REPO
AMENITY --> REPO

REPO --> DB
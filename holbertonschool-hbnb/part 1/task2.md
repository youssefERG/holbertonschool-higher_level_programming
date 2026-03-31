classDiagram

class BaseModel {
  +UUID id
  +datetime created_at
  +datetime updated_at
}

class User {
  +string first_name
  +string last_name
  +string email
  +string password
  +bool is_admin
  +register()
  +update_profile()
  +delete()
}

class Place {
  +string title
  +string description
  +float price
  +float latitude
  +float longitude
  +create()
  +update()
  +delete()
}

class Review {
  +int rating
  +string comment
  +create()
  +update()
  +delete()
}

class Amenity {
  +string name
  +string description
  +create()
  +update()
  +delete()
}

User --|> BaseModel
Place --|> BaseModel
Review --|> BaseModel
Amenity --|> BaseModel

User "1" --> "*" Place : owns
User "1" --> "*" Review : writes
Place "1" --> "*" Review : has
Place "*" --> "*" Amenity : has
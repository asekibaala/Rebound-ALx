# Movie-Actor Relationship Database

This database schema models the relationships between movies, actors, contact details, and stuntmen.

## Entities and Relationships

- **Movie**:
  - Fields: `id`, `title`, `release_date`
  - Each movie can have multiple actors.

- **Actor**:
  - Fields: `id`, `name`, `birthday`
  - Each actor can act in multiple movies.
  - Each actor has one associated contact detail and one stuntman.

- **ContactDetails**:
  - Fields: `id`, `phone_number`, `address`
  - Each actor has one set of contact details, which can include multiple phone numbers and addresses.

- **Stuntman**:
  - Fields: `id`, `name`, `active`
  - Each actor is assigned one stuntman.

## Relationships

- **Movie - Actor**: Many-to-Many (1..* : 1..*)
- **Actor - ContactDetails**: One-to-One (1 : 0..*)
- **Actor - Stuntman**: One-to-One (1 : 1)

---

This README provides a quick overview of the database structure and relationships for easier reference.
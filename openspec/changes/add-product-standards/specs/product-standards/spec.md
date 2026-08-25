# Product Standards — k-sebe-yoga

## ADDED Requirements

### Requirement: Product standards document
The repository root contains a `product-standards.md` document written in English that
captures the project's product standards on four mandatory axes: unit economics,
North Star metric, quality gate, and definition of done.

#### Scenario: The document exists and is in English
- **GIVEN** the k-sebe-yoga project
- **WHEN** the repository root is inspected
- **THEN** a `product-standards.md` file exists that is written in English

#### Scenario: The document covers the four mandatory axes
- **GIVEN** a `product-standards.md` file at the repository root
- **WHEN** its content is reviewed
- **THEN** it includes unit economics, a North Star metric, a quality gate, and a definition of done

### Requirement: OpenSpec workflow contour
The repository has an OpenSpec workflow contour (`openspec/` with `config.yaml`, `changes/`,
and `specs/`) so future changes follow the team spec→code cycle.

#### Scenario: OpenSpec contour is present
- **GIVEN** the repository
- **WHEN** the repository structure is inspected
- **THEN** an `openspec/` directory exists containing a config, a changes directory, and a specs directory

### Requirement: k-sebe-yoga North Star and unit economics
Unit economics and North Star are deferred ("TBD") until the project moves to a live/product
phase; the direction is service→product (bookings/subscription), and the likely North Star is
conversion into bookings/enquiries once live.

#### Scenario: Unit economics and North Star are explicitly marked TBD
- **GIVEN** the product standards document for k-sebe-yoga
- **WHEN** the unit-economics and North Star sections are read
- **THEN** they are marked as TBD to define when the project goes live, with the stated direction

### Requirement: k-sebe-yoga quality gate
Quality is gated by the full spec→review cycle (team canon), design rules (Lutik: text-free
images, full figure visible), and security when payments integrate.

#### Scenario: Quality gate is documented
- **GIVEN** the product standards document for k-sebe-yoga
- **WHEN** the quality-gate section is read
- **THEN** it references the full review cycle and the design rules, and security if payments are added
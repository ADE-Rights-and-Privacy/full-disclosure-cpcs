# Changelog

All releases will be logged in this file.

## [1.1.0-rc.1] - 2021-03-30

### Added
- In bulk importer: Add person-title serializer. Split date into individual components for person-grouping serializer. Add is_inactive and as_of field support for person-grouping serializer.

### Fixed
- Performance improvements for bulk import tool

### Changed
- Update Django from version 3.1.3 to 3.1.7

## [1.0.0] - 2021-03-18
First formal release, including recent changes since initial code base was established with first instance.

### Added
- Configuration specific 2FA fallback logic unitish tests
- Serializers for link between People and Grouping (e.g. career segments)

### Fixed
- 500 error on object creation pages like location and attachments (static loader)
- Fix compatibility between Django data wizard and object-based file storage backend
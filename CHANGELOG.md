# CHANGELOG

## Master

- Use the latest version of the NHS.UK frontend library ([v4.0.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#400---26-october-2020))
- Add Card blocks
- Deprecate Panel and Promo blocks
- Add visually_hidden_prefix to warning callout blocks to enable hidden text for screenreaders

## v0.4.4

- Allow h5 and h6 heading level inside all blocks that contain headings.

## v0.4.3

- Updated the do and don't panel to allow custom labels

## v0.4.2

- Use the latest version of the NHS.UK frontend library ([v3.0.4](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#304---24-march-2020))

## v0.4.1

- Make the active link in a contents-list non-clickable

## v0.4.0

- Upgrade to the nhsuk frontend library v3 (breaking changes)
  - Removed emergency alert component
  - Removed feedback banner component
- Allow sub-blocks inside Details, Expander and CareCard blocks (breaking change)
- Add summary list component
- Allow templatetags to be used without a `page` context
- Add icons to blocks for nicer streamfield UI
- Add search_action and search_field_name params to header for custom search endpoints

## v0.3.0

- New components
- Small component fixes
- Renamed "breadcrumbs" to "breadcrumb"
- Flatten component context so templates can be reused more easily


## v0.2.0

- Renamed the project from wagtail-nhs-style to wagtail-nhsuk-frontend
- Added lots of new components

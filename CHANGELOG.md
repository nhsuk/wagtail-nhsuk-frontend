# CHANGELOG

## Unreleased

- Upgrade for Wagtail 5.0+ compatibility
- Drop tests for Wagtail 4.2 and 5.0 as they have reached EOL

## 1.5.3

- Use the latest version of the NHS.UK frontend library ([v6.2.0](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md#620---17-january-2023))

## 1.5.2
- Fix for visually hidden checkbox from the warning callout component. If the title is "Important", the visually
hidden prefix is now automatically added

## 1.5.1

- Use the latest version of the NHS.UK frontend library ([v6.1.2](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#612---8-august-2022))

## 1.5.0

- Update django version to 3.2
- Remove visually hidden checkbox from the warning callout component. If the title is "Important", the visually
hidden prefix is now automatically added

## 1.4.0

- Add support for Wagtail 3.0
  
## 1.3.1

- revert migration for care card, use original types `primary`, `urgent`, `immediate` in admin, this prevents the need to edit migrations.

## 1.3.0

- Use the latest version of the NHS.UK frontend library ([v6.1.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#610---12-january-2022))
- Care card (deprecated)
- Update care card CSS class inline with the frontend library

## v1.2.4

- Do not render labels for hidden form fields 

## v1.2.3

- Fix form templatetag. Templates were missing from the python package build

## v1.2.2

- Use the latest version of the NHS.UK frontend library ([v5.2.1](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#521---28-october-2021))

## v1.2.1

- Remove static `aria-label="Open menu"` on header menu toggle. Add descriptive `aria-expanded="false"` to toggle on inital page load.

## v1.2.0

- Use the latest version of the NHS.UK frontend library ([v5.2.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#520---22-september-2021))

## v1.1.0

- Add optional default heading level setting for care cards

## v1.0.0

### Upgrade Considerations
- Deprecated blocks `PanelBlock`, `PanelList`, `GreyPanelBlock`, `PromoBlock`, `PromoGroupBlock` have been removed from the plugin.
- In order to replace these blocks with the recommended `CardBasicBlock`-type blocks, you should:
    - Upgrade to v0.8.0 or v0.7.0 where the deprecated blocks exist alongside the Card blocks.
    - Migrate `PanelBlock` and `GreyPanelBlock` to `CardFeatureBlock` as follows:
    ```
    label -> feature_heading
    heading_level -> heading_level
    body -> body
    ```
    - Migrate `PanelList` to `CardGroupBlock` by mapping `panels` to `body` with the `BodyStreamBlock` class and setting `columns` as `'one-half'`.
    - Migrate `PromoBlock` to `CardImageBlock` as follows:
    ```
    url -> url
    heading -> heading
    description -> body
    content_image -> content_image
    alt_text -> alt_text
    size -> heading_size
    heading_level -> heading_level
    ```
    - Migrate `PromoGroupBlock` to `CardGroupBlock` by mapping `promos` to `body` using the `BodyStreamBlock` class, `column` maps to `column`. `size` and `heading_level` map to their respective fields in the child Card blocks.
- After all deprecated blocks have been migrated, you can upgrade to v1.0.0 without any loss of data.

### Changes
- Add the organisational header variant
- Add form component
- Remove `PanelBlock`, `PanelList`, `GreyPanelBlock`, `PromoBlock`, `PromoGroupBlock`
- Improve test coverage

## v0.8.0

- Use the latest version of the NHS.UK frontend library ([v5.1.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#510---14-may-2021))

## v0.7.0

- Use the latest version of the NHS.UK frontend library ([v5.0.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#500---26-march-2021))

## v0.6.0

- Use the latest version of the NHS.UK frontend library ([v4.1.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#410---21-january-2021))
- Add internal page link option to ActionLink and Card blocks

## v0.5.0

- Use the latest version of the NHS.UK frontend library ([v4.0.0](https://github.com/nhsuk/nhsuk-frontend/blob/master/CHANGELOG.md#400---26-october-2020))
- Add Card blocks
- Add deprecation notice to Panel and Promo blocks
- Add visually_hidden_prefix to warning callout blocks to enable hidden text for screenreaders
- Rename the label for the Don't list in the admin panel

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

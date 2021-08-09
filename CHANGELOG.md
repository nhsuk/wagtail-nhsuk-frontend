# CHANGELOG

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

# inline-css-action

Converts HTML files to use inline styling.

## Usage

```yaml
      - uses: ZacJW/inline-css-action@1.0.0
        with:
          files: '["test.html", "dir/*.html"]'
```

This example will convert `test.html` and all `.html` files in `dir/` to use inline styling.

## Inputs

### `files`

**Required**. A JSON list of paths to html files to convert. They will be overwritten to use inline styling. Paths may be glob patterns, in which case all matching files will be converted and overwritten.

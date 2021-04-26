# RegExp cheat sheet

- 肯定先読み
  - `foo(?=bar)`
  - 直後にbarがあるfoo
- 否定先読み
  - `foo(?!bar)`
  - 直後にbarがないfoo
- 肯定後読み
  - `(?<=bar)foo`
  - 直前にbarがあるfoo
- 否定後読み
  - `(?<!bar)foo`
  - 直前にbarがないfoo

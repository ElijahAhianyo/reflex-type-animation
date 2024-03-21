# reflex-type-animation

Reflex type animation is a reflex wrapper around [react-type-animations](https://github.com/maxeth/react-type-animation)

## Installation

```bash
pip install reflex-type-animation
```

## Usage

```python
from reflex_type_animation import type_animation


def index() -> rx.Component:
    return rx.center(
        type_animation(
            sequence=[
                "The quick brown fox jumped over the lazy Dog",
                1000
            ]
        ),
    )
```

[Screen Recording 2024-03-21 at 3.11.59 PM.mov](..%2F..%2F..%2F..%2F..%2FDesktop%2FScreen%20Recording%202024-03-21%20at%203.11.59%20PM.mov)

### Props

Visit [this link](https://react-type-animation.netlify.app/options) for a more extensive 
list of prop options and their uses. However, note that the camelCase prop options are translated 
to snake_case in reflex-type-animation.

Below are the prop options and their correct translations:

| Prop                    | Name to use               |
|-------------------------|---------------------------|
| `preRenderFirstString`  | `pre_render_first_string` |
| `deletionSpeed `        | `deletion_speed `         |
| `omitDeletionAnimation` | `omit_deletion_animation` |

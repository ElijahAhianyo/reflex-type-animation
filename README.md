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



https://github.com/ElijahAhianyo/reflex-type-animation/assets/19895635/1732465f-d2c2-43f2-ac88-9d18479bd815



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

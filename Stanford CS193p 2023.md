## Lecture 14

Color vs. UIColor vs. CGColor

- ﻿﻿Color
   What this symbol means in SwiftUI varies by context.
   Is a color-specifier, e.g., • foregroundColor (Color.green).
   Can also act like a ShapeStyle, e.g., • fill(Color.blue).
   Can also act like a View, e.g., Color. white can appear wherever a View can appear.
   Due to this multifaceted role, its API is limited mostly to creation/comparison.
- ﻿﻿UIColor
   Is used to manipulate colors.
   Also has many more built-in colors than Color, including "system-related" colors.
   Can be interrogated and can convert between color spaces (RGB vs. HSB, etc.).
   Once you have desired UIColor, employ Color (uiColor:) to use it in one of the roles above.

- CGColor
   The fundamental color representation in the Core Graphics drawing system.
   Color might be able to give a CColor representation of itself (color. cColor is optional).
---
name: Guardião Laranja
colors:
  surface: '#fff8f5'
  surface-dim: '#ead6c9'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1e9'
  surface-container: '#ffeadd'
  surface-container-high: '#f9e4d7'
  surface-container-highest: '#f3dfd1'
  on-surface: '#241912'
  on-surface-variant: '#564334'
  inverse-surface: '#3a2e25'
  inverse-on-surface: '#ffede3'
  outline: '#897362'
  outline-variant: '#ddc1ae'
  surface-tint: '#904d00'
  primary: '#904d00'
  on-primary: '#ffffff'
  primary-container: '#ff8c00'
  on-primary-container: '#623200'
  inverse-primary: '#ffb77d'
  secondary: '#006a6a'
  on-secondary: '#ffffff'
  secondary-container: '#90efef'
  on-secondary-container: '#006e6e'
  tertiary: '#705d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#c7a800'
  on-tertiary-container: '#4b3e00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdcc3'
  primary-fixed-dim: '#ffb77d'
  on-primary-fixed: '#2f1500'
  on-primary-fixed-variant: '#6e3900'
  secondary-fixed: '#93f2f2'
  secondary-fixed-dim: '#76d6d5'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#ffe16d'
  tertiary-fixed-dim: '#e9c400'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#544600'
  background: '#fff8f5'
  on-background: '#241912'
  surface-variant: '#f3dfd1'
typography:
  display-hero:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Quicksand
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.6'
  body-md:
    fontFamily: Quicksand
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Quicksand
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
  label-sm:
    fontFamily: Quicksand
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style
The design system is built to balance the gravity of child protection with the engaging nature of an educational journey. The personality is **Empowering, Vigilant, and Welcoming**. It avoids being overly "childish" to maintain its status as a serious educational tool, instead adopting a **Modern Heroic** aesthetic that positions the user as a "Guardian."

The visual style leverages **Soft Minimalism** with **Tactile** accents. It uses clean layouts to ensure information density remains low and readable, while using subtle depth and symbolic "Guardian" motifs (shields and the orange gerbera flower) to provide an immersive, game-like experience. The goal is to evoke a sense of safety and agency in the user.

## Colors
The palette is dominated by **Awareness Orange**, used for primary actions, branding, and key progress indicators. This is balanced by **Safety Teal**, which provides a calming, trustworthy counterpoint for secondary information and background structures.

- **Primary (Orange):** The heartbeat of the design system. Used for call-to-action buttons, the "Guardian" icon highlights, and critical campaign information.
- **Secondary (Teal):** Used for navigation headers, utility icons, and to signify "safe" zones within the UI.
- **Accent (Yellow):** Reserved for "Optimism" highlights, such as earning points or leveling up.
- **Feedback (Green/Red):** High-contrast tones for immediate validation during the mini-game/quiz components.
- **Backgrounds:** Utilizes very light greys and whites to ensure high legibility and a "breathable" interface.

## Typography
Typography follows a dual-font strategy. **Montserrat** is used for headlines to provide a sense of strength, authority, and modernity. **Quicksand** is used for all body text and labels; its rounded terminals make the information feel accessible and friendly, reducing the anxiety often associated with sensitive topics.

Line heights are intentionally generous (1.6 for body) to assist readability for a broad age range. Bold weights are used frequently for emphasis within the educational content to ensure key safety messages are never missed.

## Layout & Spacing
This design system employs a **Fixed Grid** on desktop and a **Fluid Content Model** on mobile. 
- **Desktop:** A 12-column grid with a max-width of 1200px. Content is centered to create a focused, "theatrical" feel for the game content.
- **Mobile:** A single-column layout with 24px side margins. 
- **Rhythm:** An 8px linear scale is used. Components are separated by "lg" (48px) blocks to keep the UI from feeling cluttered. Cards use "md" (24px) internal padding to maintain a comfortable "breathing" space around text and illustrations.

## Elevation & Depth
Depth is used sparingly to define hierarchy. This system uses **Tonal Layers** combined with **Ambient Shadows**:
- **Level 0 (Background):** White or #F8F9FA.
- **Level 1 (Cards):** White surface with a very soft, diffused orange-tinted shadow (4px blur, 5% opacity).
- **Level 2 (Interactive/Buttons):** These use a more pronounced "squishy" shadow effect to appear pushable. 
- **Overlays:** Full-screen modals for quiz results use a semi-transparent Safety Teal backdrop blur (8px) to keep the user focused on the immediate feedback while maintaining context.

## Shapes
Shapes are distinctly **Rounded** (0.5rem base) to echo the friendly nature of the Quicksand typeface and the campaign's flower symbol. 
- **Buttons:** Large, pill-shaped (rounded-xl) to appear inviting and easy to tap on mobile.
- **Cards:** Standard 1rem (rounded-lg) corner radius.
- **Icons:** Enclosed in circular "Shield" frames to reinforce the Guardian theme.
- **Progress Bars:** Fully rounded ends to suggest a continuous, smooth journey.

## Components
- **Guardian Buttons:** High-saturation Orange background with white Montserrat bold text. On hover/active, they should "sink" slightly (reducing shadow) to provide tactile feedback.
- **Information Cards:** White surfaces with a Safety Teal left-border accent (4px) to denote educational content. 
- **Quiz Chips:** Used for multiple-choice answers. Neutral grey backgrounds that transition to Teal (correct) or Red (incorrect) with a slight scale-up animation upon selection.
- **Progress Indicator:** A horizontal track using a light orange base and a vibrant Primary Orange fill, punctuated by "Flower" or "Sun" icons at key milestones.
- **The "Guardian Shield":** A recurring decorative/functional element used to house iconography. It uses the Secondary Teal color to frame content.
- **Input Fields:** Soft grey backgrounds with bottom-only borders that turn Primary Orange when focused, ensuring the interface remains clean but responsive.
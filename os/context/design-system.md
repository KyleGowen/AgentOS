# UI and Frontend Design System

This file is the canonical global design-system preference for Kyle's UIs,
frontends, and reusable visual components.

## Default

- Use [shadcn/ui](https://ui.shadcn.com/) as the default design system and
  component foundation for UI and frontend work.
- Prefer importing and composing the actual shadcn/ui components when the
  project's framework and dependency constraints allow it.
- If shadcn/ui cannot reasonably be imported, design the interface to look and
  behave like shadcn/ui: quiet, polished, accessible components; consistent
  tokens and spacing; restrained borders and radii; clear hierarchy; and
  predictable interaction states.
- Apply this preference to pages, application shells, navigation, forms,
  dialogs, tables, cards, dashboards, feedback states, and reusable components.
- Preserve responsive desktop and mobile behavior and accessibility while
  following the visual system.

## Inheritance

This is a global cross-project preference. AgentOS-aware subprojects should
include it in their inherited global-rules cache or otherwise reference this
file with provenance to committed `KyleGowen/AgentOS` `main`.

Repository-specific instructions may override this preference when an existing
product design system, customer requirement, technical constraint, or explicit
Kyle instruction requires a different result. Record or report a material
override instead of silently treating it as the default.


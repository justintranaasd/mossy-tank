// Central site config — edit brand details here.
export const SITE_TITLE = 'Mossy Tank';
export const SITE_TAGLINE = 'Low-tech planted tanks, made easy.';
export const SITE_DESCRIPTION =
  'Beginner-friendly guides to low-tech planted aquariums, betta and shrimp tanks — no CO2, no jargon, no killed fish. Honest gear picks and step-by-step help.';
export const SITE_URL = 'https://mossytank.com';
export const AUTHOR = 'The Mossy Tank Team';
export const CONTACT_EMAIL = 'hello@mossytank.com';

// Primary nav (content clusters from the plan).
export const NAV_LINKS = [
  { href: '/blog/', label: 'Guides' },
  { href: '/about/', label: 'About' },
  { href: '/contact/', label: 'Contact' },
];

// Content clusters (used for tagging + future category pages).
export const CLUSTERS = {
  'low-tech': 'Low-Tech Planted Tanks',
  betta: 'Planted Betta Tanks',
  'shrimp-nano': 'Shrimp & Nano Tanks',
  plants: 'Aquarium Plants',
  troubleshooting: 'Troubleshooting',
  gear: 'Gear & Buying Guides',
  general: 'General',
} as const;

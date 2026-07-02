// Phone-number detection for the audit's tel_missing check.
//
// The old pattern /(?:\+?\d[\d\s().-]{7,}\d)/ fired on ISBNs, dates and prices
// (proven false-positive on a Wikipedia article), which produced a HIGH
// "phone number is not tappable" finding on pages with no phone at all.
// This module errs toward fewer false positives: a digit run only counts as a
// phone when it is (a) +international, (b) 0-lead national, or (c) clearly
// phone-grouped — and never when it is shaped like a date, an ISBN or a
// thousands-grouped number.

// Candidate extraction: a digit run with phone separators, not embedded in a
// longer digit/letter run (lookarounds reject e.g. the tail of an SKU or a
// substring of a longer number).
const CANDIDATE_SRC = String.raw`(?<![\w+.-])(\+?\(?\d[\d\s().-]{5,18}\d)(?![\w-])`;

// True when a single extracted candidate string is plausibly a phone number.
export function isPhoneLike(candidate) {
  const s = String(candidate || '').trim();
  const digits = s.replace(/\D/g, '');
  if (digits.length < 8 || digits.length > 15) return false;

  // Date shapes: 2026-07-02 / 02.07.2026 — also when wrapped in parentheses,
  // e.g. Wikipedia citation dates "(2012-02-21)".
  const bare = s.replace(/[()\s]/g, '');
  if (/^\d{4}[-./]\d{1,2}[-./]\d{1,2}$/.test(bare)) return false;
  if (/^\d{1,2}[-./]\d{1,2}[-./]\d{4}$/.test(bare)) return false;

  // International prefix is the strongest phone signal.
  if (s.startsWith('+')) return true;

  const zeroLead = /^\(?0/.test(s);
  const groups = s.replace(/[()]/g, ' ').split(/[\s.-]+/).filter(Boolean);
  const groupsOk = groups.length > 0 && groups.every((g) => /^\d{2,4}$/.test(g));

  // Thousands-grouped number (12.500.000 / 12 345 678): not a phone.
  // (Phones never lead with a bare 1-3 digit group followed by all-3 groups
  // unless 0-lead, e.g. 069 123 456, which is checked first below.)
  if (!zeroLead && groups.length >= 2 && /^\d{1,3}$/.test(groups[0]) &&
      groups.slice(1).every((g) => g.length === 3)) return false;

  // ISBN-ish runs (978-0-306-40615-7) fail the 2-4-digit group rule.
  if (zeroLead) return groups.length === 1 || groupsOk; // 069123456 or 0722-123-456
  return groups.length >= 3 && groupsOk; // (312) 555-0199, 123-456-7890
}

// True when the text (HTML with <script> blocks already stripped) shows
// something that plausibly reads as a phone number.
export function hasVisiblePhone(text) {
  const s = String(text || '');
  const re = new RegExp(CANDIDATE_SRC, 'g');
  let m;
  while ((m = re.exec(s)) !== null) {
    if (isPhoneLike(m[1])) return true;
  }
  return false;
}

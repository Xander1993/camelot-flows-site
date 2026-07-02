// Tests for the audit's phone-number heuristic: functions/_lib/audit-phone.mjs
// Run: node --test tests/phone.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { isPhoneLike, hasVisiblePhone } from '../functions/_lib/audit-phone.mjs';

test('plausible phone formats are detected', () => {
  const phones = [
    '+373 69 123 456',
    '(312) 555-0199',
    '0722-123-456',
    '069 123 456',
    '069123456',
    '123-456-7890',
    '+1 (312) 555-0199',
  ];
  for (const p of phones) {
    assert.equal(hasVisiblePhone('Call us: ' + p + ' today'), true, 'should match: ' + p);
  }
});

test('ISBNs, dates and prices are NOT phones', () => {
  const notPhones = [
    'ISBN 978-0-306-40615-7',
    'ISBN 9780306406157',
    'published 2026-07-02',
    'on 02.07.2026 at noon',
    'costs 1,234,567 lei',
    'price 12.500.000 lei',
    'population 12 345 678 people',
    'copyright 2020-2026',
    'pi is 3.14159265358979',
    'Winterton, Deanne (2012-02-21). Retrieved 2026-07-02.', // citation-style parenthesised date
  ];
  for (const s of notPhones) {
    assert.equal(hasVisiblePhone(s), false, 'should NOT match: ' + s);
  }
});

test('digit runs embedded in longer digit/letter runs are ignored', () => {
  assert.equal(hasVisiblePhone('order SKU98123456789X shipped'), false);
  assert.equal(hasVisiblePhone('img-1200x800.jpg?v=20260702123456'), false);
});

test('isPhoneLike unit cases', () => {
  assert.equal(isPhoneLike('+373 69 123 456'), true);
  assert.equal(isPhoneLike('(312) 555-0199'), true);
  assert.equal(isPhoneLike('0722-123-456'), true);
  assert.equal(isPhoneLike('978-0-306-40615-7'), false); // ISBN grouping
  assert.equal(isPhoneLike('2026-07-02'), false); // date
  assert.equal(isPhoneLike('1234567'), false); // too few digits
  assert.equal(isPhoneLike('12345678901234567890'), false); // too many digits
  assert.equal(isPhoneLike('12345678'), false); // bare ungrouped run, no + / 0 lead
});

test('hasVisiblePhone finds a real phone even after false-positive shapes', () => {
  const html = 'ISBN 978-0-306-40615-7, updated 2026-07-02. Contact: +373 69 123 456';
  assert.equal(hasVisiblePhone(html), true);
});

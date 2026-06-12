// Tests for the audit tool's LLM A/B helpers: functions/_lib/llm.mjs
// Run: node --test tests/llm.test.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { pickModel, buildLlmMessages } from '../functions/_lib/llm.mjs';

test('pickModel deterministically maps rand to each configured model', () => {
  const models = ['deepseek/deepseek-v4-flash', 'nousresearch/hermes-4-70b'];
  assert.equal(pickModel(models, 0.1), 'deepseek/deepseek-v4-flash');
  assert.equal(pickModel(models, 0.9), 'nousresearch/hermes-4-70b');
});

test('buildLlmMessages includes findings, score and url', () => {
  const findings = [{ id: 'no_viewport', severity: 'medium', title: 'No viewport', detail: 'd' }];
  const msgs = buildLlmMessages(findings, 'https://acme.com/', 80);
  const all = JSON.stringify(msgs);
  assert.ok(all.includes('no_viewport'));
  assert.ok(all.includes('acme.com'));
  assert.ok(all.includes('80'));
});

test('buildLlmMessages forbids inventing findings and starts with a system role', () => {
  const msgs = buildLlmMessages([], 'https://acme.com/', 100);
  assert.equal(msgs[0].role, 'system');
  assert.ok(/only|solely|strictly/i.test(msgs[0].content));
  assert.equal(msgs[1].role, 'user');
});

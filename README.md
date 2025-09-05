# Compressed Standalone Parsers Issue Showcase

This repository demonstrates an issue encountered with compressed standalone parsers. The goal is to highlight the discrepancy between expected and actual results when using such parsers, and to provide steps to reproduce and fix the issue.

## Table of Contents

- [Compressed Standalone Parsers Issue Showcase](#compressed-standalone-parsers-issue-showcase)
  - [Expected Result](#expected-result)
  - [Actual Result](#actual-result)
  - [How to Reproduce](#how-to-reproduce)
  - [Issue](#issue)
  - [Solution](#solution)
    - [Implementation](#implementation)

## Expected Result

```bash
>>> 2 + 2
4
>>> (3 * 5) - 1
14
>>> 10 / 2
5.0
```

## Actual Result

```bash
ModuleNotFoundError: No module named 'lark'
```

## How to Reproduce

```bash
$ uv run --no-cache --isolated --package calculator-repr calc
```

## Issue

The issue arises because the compressed standalone parser relies on certain components of the `lark` library that are embedded within the standalone module. However, when attempting to unpickle the parser, Python's `pickle` module expects the `lark` library to be installed in the environment. This discrepancy leads to the `ModuleNotFoundError` when the `lark` library is not available.

## Solution

To resolve this issue, you can use a custom unpickler class that checks the resolution module. If the module matches the copied files, it replaces them with the standalone module. This ensures that the standalone parser functions correctly without requiring the `lark` library to be installed in the environment.

This approach ensures that the standalone parser resolves dependencies correctly, avoiding the `ModuleNotFoundError`.

### Implementation

For more details on the implementation and the fix, refer to the [GitHub repository](https://github.com/mikebohdan/lark/tree/standalone-compress-fix). You can test the solution using the following command:

```bash
uv run --no-cache --isolated --package calculator-repr calc
```

This command ensures that the environment is isolated and does not rely on cached dependencies, allowing you to verify the fix in a clean setup.

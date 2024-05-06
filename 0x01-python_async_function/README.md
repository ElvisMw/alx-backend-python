# Asynchronous Programming in Python with asyncio

This project demonstrates asynchronous programming in Python using the asyncio library. It consists of several tasks designed to introduce and practice asynchronous concepts.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Tasks](#tasks)
    - [Task 1: The Basics of Async](#task-1-the-basics-of-async)
    - [Task 2: Executing Multiple Coroutines Concurrently](#task-2-executing-multiple-coroutines-concurrently)
    - [Task 3: Measuring Runtime](#task-3-measuring-runtime)
    - [Task 4: Creating asyncio Tasks](#task-4-creating-asyncio-tasks)
4. [Usage](#usage)
5. [License](#license)

## Introduction

This project aims to provide practical examples of asynchronous programming in Python using asyncio. Each task builds upon the previous one, covering topics such as asynchronous coroutines, concurrent execution, and measuring runtime performance.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- pycodestyle 2.5.x

## Tasks

### Task 1: The Basics of Async

Write an asynchronous coroutine that generates a random delay between 0 and a specified maximum delay.

### Task 2: Executing Multiple Coroutines Concurrently

Create an async routine that spawns multiple instances of the coroutine from Task 1 simultaneously and returns the list of delays in ascending order.

### Task 3: Measuring Runtime

Implement a function to measure the total execution time for running the coroutines created in Task 2 and return the average time per coroutine.

### Task 4: Creating asyncio Tasks

Create asyncio Tasks for the coroutines defined in Task 1 and Task 2

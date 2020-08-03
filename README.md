# venpo

Extract Venmo transactions from a profile with one command

## Demo

Make demo here

## About

A simple command line tool to extract public Venmo transactions from a specified user profile.

venpo will access a Venmo user's profile page, extract the transactions, and save to a JSON file.

## Use Cases

1. Save a history of your own or a friend's Venmo transactions
2. Transaction monitoring for OSINT (open source intelligence) purposes
3. Collecting data to train your own ML model


## Installation

```shell script
$ pip install venpo --upgrade
```

## Usage

```shell script
$ venpo $username
```
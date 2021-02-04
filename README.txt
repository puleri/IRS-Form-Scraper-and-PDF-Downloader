# IRS Form Scraper and PDF Downloader

## Objectives

The code in IRS_Form_Scraper.py and PDF_downlader.py will:

- Convert form data on search results at [the IRS form site](https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+W-2&criteria=formNumber&submitSearch=Find)
  to JSON
- Search and download PDFs in the given range of years from page in sub-directory

## Preparation

1. Fork and clone this repository.
 [FAQ](https://git.generalassemb.ly/ga-wdi-boston/meta/wiki/ForkAndClone)
1. Create a new branch, `training`, for your work.
1. Checkout to the `training` branch.
1. Install dependencies with `npm install`.

## Callbacks

A callback is a function that we pass as an argument to another function or
method.  This other function invokes the callback as a necessary part of
accomplishing its task.  The JavaScript Array Iteration Methods require callback
functions.

We often use **predicate** functions, functions returning either
`true` or `false`, as callbacks. A common convention for predicate functions
is to prefix them with **is** (ex. `isOn`, `isOnTrack`, or `isRotten`)

See [bin/callbacks.js](bin/callbacks.js) for an example.

## Arrow Functions

We frequently use `arrow functions` (sometimes called fat arrow functions) as
callbacks with array iteration methods.  This is convenient when the callback is
simple and anonymous.

### Code Along: Rewriting Functions Expressions As Arrow Functions

Let's rewrite the following functions as arrow functions in [bin/arrow-functions.js](bin/arrow-functions.js)

#### How to Convert to Arrow Function Syntax

We can convert an existing JavaScript function to use the arrow function syntax
with the following steps.

1. Remove the `function` keyword
2. Add an arrow (`=>`) between the function parameters  `()` and the opening
    brace `{`

```js
// Without arrow function syntax
const helloWorld = function () {
  console.log('Hello World!')
}

// Using arrow function syntax
const helloWorld = () => {
  console.log('Hello World!')
}
```

##### Single Expression Implicit Return

Arrow functions bodies that are a single expression have an added benefit, an
implicit return.  This means that arrow function bodies without `{}` return the
value of the expression without needing to use `return`.

```js
// Without arrow function syntax
const add = function (x, y) {
  return x + y
}

// Using arrow function syntax with an explicit return
const add = (x, y) => {
  return x + y
}

// Using arrow function syntax with an implicit return
const add = (x, y) => x + y
```

##### Single Parameter

When using the arrow function syntax with a single parameter, then parenthesis
 are not required.

```js
// Without arrow function syntax
const isPositive = function (num) {
  return num > 0
}

// Using arrow function syntax with an implicit return value
const isPositive = (num) => num > 0

// Parenthesis aren't required for a single parameter
const isPositive = num => num > 0
```

### Lab: Converting To Arrow Function Syntax

Now it's your turn. Convert the function in [bin/arrow-lab.js](bin/arrow-lab.js)
 to use arrow function syntax.

### Arrow Function Caveats

Arrow functions have a few caveats.

Arrow functions:

- **cannot** be used as a Constructor (`new` does not bind `this`, no
  `prototype` property).
- always have a lexically bound `this` (we'll learn more about that later).

## Array Iteration Methods

We'll explore the array methods that allow us to test and transform arrays more
simply and consistently, [Iteration
methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Iteration_methods),
and optionally at the end, we'll model some of these JavaScript Array methods as
functions. Being able to use these methods correctly is our main goal.

We'll check our work in `node` or using the scripts in `bin/`.

There are two main groups of array iteration methods:

1. Those that must process all of the array elements
1. Those that may only process a subset of the array elements

### Processing all array elements

#### Code along: using `forEach`

The
[forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
method iterates over all of the elements in an array. Unlike a `for` loop, it
cannot be stopped (all elements are processed).  `forEach` returns `undefined`.

From the MDN documentation:

> There is no way to stop or break a `forEach()` loop other than by throwing an
> exception. If you need such behavior, the `forEach()` method is the wrong
> tool, use a plain loop instead. If you are testing the array elements for a
> predicate and need a Boolean return value, you can use `every()` or `some()`
> instead. If available, the new methods `find()` or `findIndex()` can be used
> for early termination upon true predicates as well.

This means that `forEach` is a poor choice for an array operation that may
terminate early.

#### Code along: using `map`

The
[map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
method returns a **new** array the same size as the existing array.  The
elements of the new array are set to the return value of the callback passed to
`map` invoked with the corresponding element from the original array as its
argument (e.g. `newArray[i] = callback(array[i])`).  The array `map` is called
upon is **not** mutated.

#### Lab: using `filter`

The
[filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
method returns a **new** array containing elements from the original array for
which the callback returns `true`.  `filter` uses a predicate callback method to
decide on which elements to add to the new array that it returns. The length of
the new array may be 0 if the callback returned `false` for every element, or
equal to the length of the original array, if the callback returned `true` for
every element in the original array.

Callbacks passed to `filter` should be predicate functions.

### Processing a subset of the array elements

#### Demo: using `findIndex`

The
[findIndex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)
method returns the index of the first element in the array for which the
callback returns true.

Why do we need `findIndex`?  Why not just use
[indexOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)?

#### Code along: using `find`

The
[find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)
method returns the first element in the array for which the callback returns
true.

#### Code along: using `some`

The
[some](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)
method return true if the callback returns `true` for any element of the array.

Callbacks passed to `some` should be predicate functions.

#### Lab: using `every`

The [every](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)
method checks to see if all elements of the array meet some test.  The function
used for this should only return `true` or `false`.  This type of function is
often called a predicate.

Callbacks passed to `every` should be predicate functions.

## Additional Resources

- [Array Iteration Method Practice Problems](extra-practice.md)
- [Array Methods Explained: filter, map, reduce, & forEach](https://codeburst.io/array-methods-explained-filter-vs-map-vs-reduce-vs-foreach-ea3127c6d319)
- [Array Method Explorer](https://sdras.github.io/array-explorer/)
- [W3Schools Array Iteration Methods](https://www.w3schools.com/js/js_array_iteration.asp)
- [How to use Array Iteration Methods | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-array-methods-in-javascript-iteration-methods)
- [:movie_camera: JavaScript Array Methods Playlist - The Coding Train](https://www.youtube.com/watch?v=H4awPsyugS0&list=PLRqwX-V7Uu6aAEUqu96Newc-7qpuh-cxc)
- [:movie_camera: Array Iteration: Methods - freeCodeCamp](https://www.youtube.com/watch?v=Urwzk6ILvPQ)
- [Array Iteration Method Challenge Problems](extra-challenge.md)

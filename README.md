# py-yummy

Because `import bacon` really ought to be a thing...

```
Python 3.7.0 (default, Jul 23 2018, 20:22:55)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import yummy

In [2]: import bacon

yum, bacon...
Eggs in Bacon Baskets Recipe
   (http://www.seriouseats.com/recipes/2013/04/eggs-in-a-bacon-basket-recipe.html)
 - 8 eggs
 - 8 slices bacon

In [3]: bacon.open()  # View the recipe
Out[3]: True
```

## Usage

1. Create and activate virtual environment.
2. Install requirements.  Requirements are managed via [Poetry](https://github.com/sdispater/poetry), but, for simplicity, they're also exported to a `requirements.txt` file.
    ```
    pip install -Ur requirements.txt
    ```
3. Py-Yummy uses Edamam as its recipes API.  Sign up for a developer account at https://developer.edamam.com/, then create a `.env` file with your app ID and key.
    ```
    EDAMAM_APP_ID=secret_id
    EDAMAM_APP_KEY=secret_key
    ```
4. Run it in IPython or bpython.
    ```
    ipython
    import yummy
    import chocolate_brownies
    ```

## Known Issues

1. It doesn't have any error handling, because it's silly.
2. It's not published on PyPI, because it's silly, and so publishing it would be silly.

## Why?

This started as a joke on the [KnoxDevs](https://knoxdevs.com/) Slack.  But it was a good excuse to try out [Poetry](https://github.com/sdispater/poetry) for package management, [monkey around with how Python loads modules](https://stackoverflow.com/q/43571737/25507), and [show recipe images in the console](https://jart.github.io/fabulous/).
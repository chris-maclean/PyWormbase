# wormbase_parasite
This package is an interface to the WormBase ParaSite REST API. You can use it in your Python programs to retrieve data from the WormBase ParaSite REST API without needing to learn the details of REST API interactions. The function names are intelligent and documentation is provided. This package is targeted toward Wormbase users who want to get data from WormBase faster than using the web site.

## Installation
Installation is simple with `pip`. Simply run

```Python
> pip install wormbase-parasite
```

to retrieve this package from the PyPI package index.

## Usage
The WormBase ParaSite REST API is free and open. No credentials, keys, or tokens are needed to access it. This makes PyWormbase easy to use in scripts, too. First, import `pywormbase`, then instantiate a `WormbaseClient` object:

```Python
>>> import wormbase_parasite
>>> api = wormbase_parasite.WormbaseClient()
```

A `WormbaseClient` object will have a variety of member functions that provide access to Wormbase API endpoints. You can use `dir(api)` to see all functions available (or read the associated documentation in the Github wiki).

## Support
If you use PyWormbase and are experiencing problems with the package, or if you have a request for an additional feature, please file an issue at https://github.com/c-anna/PyWormbase/issues.

A note: `wormbase_parasite` is a wrapper around the WormBase ParaSite REST API. This API is subject to change and so both the content and format of the responses may change without notice. While every effort will be made to keep this package aligned with the output of the REST API, it is still possible for scripts relying on this package to change their execution results even if no code changes were made. If you use `wormbase_parasite` and notice a change in a function's execution, please open an issue on Github.

## License
`wormbase_parasite` is free and open-source, licensed under the GPLv3 license.

```
     . .  .  .  . . .
   .                     .                _.-/`/`'-._
   . Thanks for using     .             /_..--''''_-'
    . wormbase_parasite! .             //        \
     . .  .  .     .                  //-.__\_\.-'
                `..'  _\\\//  --.___ // ___.---.._
                  _- /@/@\  \       ||``          `-_
                .'  ,\_\_/   |    \_||_/      ,-._   `.
               ;   { o    /   }     ""        `-._`.   ;
              ;     `-==-'   /                    \_|   ;
             |        |>o<|  }@@@}                       |
             |       <(___<) }@@@@}                      |
             |       <(___<) }@@@@@}                     |
             |        <\___<) \_.?@@}                    |
              ;         V`--V`__./@}                    ;
               \      tx      ooo@}                    /
                \                                     /
                 `.                                 .'
                   `-._                         _.-'
                       ``------'''''''''------``
```


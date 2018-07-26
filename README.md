# PyWormbase
This package is an interface to the WormBase REST API. You can use it in your Python programs to retrieve data from the WormBase API without needing to learn the details of REST API interactions. The function names are intelligent and documentation is provided. This package is targeted toward Wormbase users who want to get data from Wormbase faster than using the web site.

## Installation
Installation is simple with `pip`. Simply run

```Python
> pip install pywormbase
```

to retrieve this package from the PyPI package index.

## Usage
Wormbase's API is free and open. No credentials, keys, or tokens are needed to access it. This makes PyWormbase easy to use in scripts, too. First, import PyWormbase, then instantiate a WormbaseClient object:

```Python
>>> import pywormbase
>>> api = pywormbase.WormbaseClient()
```

A `WormbaseClient` object will have a variety of member functions that provide access to Wormbase API endpoints. You can use `dir(api)` to see all functions available (or read the associated documentation in the Github wiki).

## Support
If you use PyWormbase and are experiencing problems with the package, or if you have a request for an additional feature, please file an issue at https://github.com/c-anna/PyWormbase/issues.

## License
PyWormbase is free and open-source, licensed under the MIT license. If you are using this software academically or professionally, please acknowledge this package and my Github page, https://github.com/c-anna, somewhere in your final product. 

```
     . .  .  .  . . .
   .                  .                   _.-/`/`'-._
   . Thanks for using!.                 /_..--''''_-'
    .    PyWormbase! .                 //        \
     . .  .  .      .`                //-.__\_\.-'
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


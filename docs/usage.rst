=====
Usage
=====

Usage is simple:

  - Install it with :cmd:`pip install eidreader`
    
  - Run the :cmd:`eidreader` command::

        $ eidreader
        {'version': '0.0.4', 'error': 'CKR_TOKEN_NOT_PRESENT
        (0x000000E0)', 'country': 'BE'}

  - Insert a Belgian eID card into your reader and run the command
    again::
    
        $ eidreader 
        {'version': '0.0.4', 'card_data': {...}, 'country': 'BE'}

    which dumps the data to stdout by
    default.
  
        

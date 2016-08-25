==========
Contribute
==========

Suggestions, reported and documented issues are welcome.

To contribute to this repositorty, please contact to sysadmin@softbutterfly.space
in ordes to request permission.

Once permisions are granted to you configure yor local repository and use
``commit.template`` file as the template for makign commits. You can set this
file as your git's ``commit.template`` by following this commands

.. code-block:: bash

    $ cd /path/to/adricolors
    $ git config --local commit.template $(pwd)/commit.template

After that, you will need add your changes and commit in the following way

.. code-block:: bash

    $ git add .
    $ git commit
    $ # Do the necessary changes and fill the requested information
    $ git commit -F .git/COMMIT_EDITMSG

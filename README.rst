A Python sample package
=======================================================================

.. code-block:: bash

  $ something-here

Also see `<https://github.com/alexisbellido/dockerize-django/tree/master/basic-python>`_.

If using setup() in setup.py with dependency_links like this:

.. code-block:: bash

  install_requires = [
      'znbsample==0.1.dev1'
  ],
  dependency_links = [
      'git+https://github@github.com/alexisbellido/znbsample.git/@master#egg=znbsample-0.1.dev1'
  ]

You need to use pip with --process-dependency-links

.. code-block:: bash

  $ pip install --process-dependency-links /root/Projects/znbpackage

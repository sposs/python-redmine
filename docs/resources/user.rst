User
====

Supported by Redmine starting from version 1.1

Manager
-------

All operations on the User resource are provided by its manager. To get access
to it you have to call ``redmine.user`` where ``redmine`` is a configured redmine
object. See the :doc:`../configuration` about how to configure redmine object.

Create methods
--------------

create
++++++

.. py:method:: create(**fields)
   :module: redminelib.managers.ResourceManager
   :noindex:

   Creates new User resource with given fields and saves it to the Redmine.

   :param string login: (required). User login.
   :param string password: (optional). User password.
   :param string firstname: (required). User name.
   :param string lastname: (required). User surname.
   :param string mail: (required). User email.
   :param int auth_source_id: (optional). Authentication mode id.
   :param string mail_notification:
    .. raw:: html

       (optional). Type of mail notification, one of:

    - all
    - selected
    - only_my_events
    - only_assigned
    - only_owner
    - none

   :param list notified_project_ids: (optional). Project IDs for a "selected" mail notification type.
   :param bool must_change_passwd: (optional). Whether user must change password.
   :param bool generate_password: (optional). Whether to generate password for the user.
   :param bool send_information: (optional). Whether to send account information to the user.
   :param list custom_fields: (optional). Custom fields as [{'id': 1, 'value': 'foo'}].
   :param bool admin: (optional). Whether to give admin privileges to the user, requires Redmine >= 4.0.0.
   :return: :ref:`Resource` object

.. code-block:: python

   >>> user = redmine.user.create(
   ...     login='jsmith',
   ...     password='qwerty',
   ...     firstname='John',
   ...     lastname='Smith',
   ...     mail='john@smith.com',
   ...     auth_source_id=1,
   ...     mail_notification='selected',
   ...     notified_project_ids=[1, 2],
   ...     must_change_passwd=True,
   ...     custom_fields=[{'id': 1, 'value': 'foo'}, {'id': 2, 'value': 'bar'}]
   ... )
   >>> user
   <redminelib.resources.User #32 "John Smith">

new
+++

.. py:method:: new()
   :module: redminelib.managers.ResourceManager
   :noindex:

   Creates new empty User resource but saves it to the Redmine only when ``save()`` is called, also
   calls ``pre_create()`` and ``post_create()`` methods of the :ref:`Resource` object. Valid attributes
   are the same as for ``create()`` method above.

   :return: :ref:`Resource` object

.. code-block:: python

   >>> user = redmine.user.new()
   >>> user.login = 'jsmith'
   >>> user.password = 'qwerty'
   >>> user.firstname = 'John
   >>> user.lastname = 'Smith'
   >>> user.mail = 'john@smith.com'
   >>> user.auth_source_id = 1
   >>> user.mail_notification = 'selected'
   >>> user.notified_project_ids = [1, 2]
   >>> user.must_change_passwd = True
   >>> user.custom_fields = [{'id': 1, 'value': 'foo'}, {'id': 2, 'value': 'bar'}]
   >>> user.save()
   <redminelib.resources.User #32 "John Smith">

Read methods
------------

get
+++

.. py:method:: get(resource_id, **params)
   :module: redminelib.managers.ResourceManager
   :noindex:

   Returns single User resource from Redmine by its id.

   :param int resource_id: (required). Id of the user.
   :param list include:
    .. raw:: html

       (optional). Fetches associated data in one call. Accepted values:

    - memberships
    - groups

   :return: :ref:`Resource` object

.. code-block:: python

   >>> user = redmine.user.get(17, include=['memberships', 'groups'])
   >>> user
   <redminelib.resources.User #17 "John Smith">

.. hint::

   You can easily get the details of the user whose credentials were used to access the API:

   .. code-block:: python

      >>> user = redmine.user.get('current')
      >>> user
      <redminelib.resources.User #17 "John Smith">

.. hint::

   User resource object provides you with on demand includes. On demand includes are the
   other resource objects wrapped in a :ref:`ResourceSet` which are associated with a User
   resource object. Keep in mind that on demand includes are retrieved in a separate request,
   that means that if the speed is important it is recommended to use ``get()`` method with
   ``include`` keyword argument. On demand includes provided by the User resource object
   are the same as in the ``get()`` method above:

   .. code-block:: python

      >>> user = redmine.user.get(17)
      >>> user.groups
      <redminelib.resultsets.ResourceSet object with Group resources>

.. hint::

   User resource object provides you with some relations. Relations are the other
   resource objects wrapped in a :ref:`ResourceSet` which are somehow related to a User
   resource object. The relations provided by the User resource object are:

   * time_entries
   * issues (alias to issues_assigned)
   * issues_assigned (requires Python-Redmine v2.5.0)
   * issues_authored (requires Python-Redmine v2.5.0)
   * deals (requires Pro Edition and `CRM plugin <https://www.redmineup.com/pages/plugins/crm>`_)
   * contacts (requires Pro Edition and `CRM plugin <https://www.redmineup.com/pages/plugins/crm>`_)
   * invoices (requires Pro Edition and `Invoices plugin <https://www.redmineup.com/pages/plugins/invoices>`_
     >= 4.1.3)
   * expenses (requires Pro Edition and `Invoices plugin <https://www.redmineup.com/pages/plugins/invoices>`_
     >= 4.1.3)
   * products (requires Pro Edition and `Products plugin <https://www.redmineup.com/pages/plugins/products>`_
     >= 2.1.5)
   * orders (requires Pro Edition and `Products plugin <https://www.redmineup.com/pages/plugins/products>`_
     >= 2.1.5)

   .. code-block:: python

      >>> user = redmine.user.get(17)
      >>> user.issues
      <redminelib.resultsets.ResourceSet object with Issue resources>

all
+++

.. py:method:: all(**params)
   :module: redminelib.managers.ResourceManager
   :noindex:

   Returns all User resources from Redmine.

   :param int limit: (optional). How much resources to return.
   :param int offset: (optional). Starting from what resource to return the other resources.
   :return: :ref:`ResourceSet` object

.. code-block:: python

   >>> users = redmine.user.all(offset=10, limit=100)
   >>> users
   <redminelib.resultsets.ResourceSet object with User resources>

filter
++++++

.. py:method:: filter(**filters)
   :module: redminelib.managers.ResourceManager
   :noindex:

   Returns User resources that match the given lookup parameters.

   :param int status:
    .. raw:: html

       (optional). Get only users with given status. One of:

    - 0 - anonymous
    - 1 - active (default)
    - 2 - registered
    - 3 - locked

   :param string name: (optional). Filter users on their login, firstname, lastname and mail. If the
    pattern contains a space, it will also return users whose firstname match the
    first word or lastname match the second word.
   :param int group_id: (optional). Get only members of the given group.
   :param int limit: (optional). How much resources to return.
   :param int offset: (optional). Starting from what resource to return the other resources.
   :return: :ref:`ResourceSet` object

.. code-block:: python

   >>> users = redmine.user.filter(offset=10, limit=100, status=3)
   >>> users
   <redminelib.resultsets.ResourceSet object with User resources>

.. hint::

   You can also get users from a Group resource object directly using ``users`` on demand includes:

   .. code-block:: python

      >>> group = redmine.group.get(524)
      >>> group.users
      <redminelib.resultsets.ResourceSet object with User resources>

Update methods
--------------

update
++++++

.. py:method:: update(resource_id, **fields)
   :module: redminelib.managers.ResourceManager
   :noindex:

   Updates values of given fields of a User resource and saves them to the Redmine.

   :param int resource_id: (required). User id.
   :param string login: (optional). User login.
   :param string password: (optional). User password.
   :param string firstname: (optional). User name.
   :param string lastname: (optional). User surname.
   :param string mail: (optional). User email.
   :param int status:
    .. raw:: html

       (optional). User status, one of:

    - 1 - active
    - 2 - registered
    - 3 - locked

   :param int auth_source_id: (optional). Authentication mode id.
   :param string mail_notification:
    .. raw:: html

       (optional). Type of mail notification, one of:

    - all
    - selected
    - only_my_events
    - only_assigned
    - only_owner
    - none

   :param list notified_project_ids: (optional). Project IDs for a "selected" mail notification type.
   :param bool must_change_passwd: (optional). Whether user must change password.
   :param bool generate_password: (optional). Whether to generate password for the user.
   :param bool send_information: (optional). Whether to send account information to the user.
   :param list custom_fields: (optional). Custom fields as [{'id': 1, 'value': 'foo'}].
   :param bool admin: (optional). Whether to give admin privileges to the user, requires Redmine >= 4.0.0.
   :return: True

.. code-block:: python

   >>> redmine.user.update(
   ...     1,
   ...     login='jsmith',
   ...     password='qwerty',
   ...     firstname='John',
   ...     lastname='Smith',
   ...     mail='john@smith.com',
   ...     status=3,
   ...     auth_source_id=1,
   ...     mail_notification='selected',
   ...     notified_project_ids=[1, 2],
   ...     must_change_passwd=True,
   ...     custom_fields=[{'id': 1, 'value': 'foo'}, {'id': 2, 'value': 'bar'}]
   ... )
   True

.. hint::

   By default Python-Redmine uses ``/users/ID`` API endpoint which requires admin privileges, it is also
   possible to use ``/my/account`` endpoint which doesn't by using ``me`` as an ID (requires Redmine >= 4.1.0):

   .. code-block:: python

      >>> redmine.user.update('me', firstname='John')
      True

save
++++

.. py:method:: save(**attrs)
   :module: redminelib.resources.User
   :noindex:

   Saves the current state of a User resource to the Redmine. Attrs that
   can be changed are the same as for ``update()`` method above.

   :return: :ref:`Resource` object

.. code-block:: python

   >>> user = redmine.user.get(1)
   >>> user.login = 'jsmith'
   >>> user.password = 'qwerty'
   >>> user.firstname = 'John'
   >>> user.lastname = 'Smith'
   >>> user.mail = 'john@smith.com'
   >>> user.status = 3
   >>> user.auth_source_id = 1
   >>> user.mail_notification = 'selected'
   >>> user.notified_project_ids = [1, 2]
   >>> user.must_change_passwd = True
   >>> user.custom_fields = [{'id': 1, 'value': 'foo'}, {'id': 2, 'value': 'bar'}]
   >>> user.save()
   <redminelib.resources.User #1 "John Smith">

.. versionadded:: 2.1.0 Alternative syntax was introduced.

.. code-block:: python

   >>> user = redmine.user.get(1).save(
   ...     login='jsmith',
   ...     password='qwerty',
   ...     firstname='John',
   ...     lastname='Smith',
   ...     mail='john@smith.com',
   ...     status=3,
   ...     auth_source_id=1,
   ...     mail_notification='selected',
   ...     notified_project_ids=[1, 2],
   ...     must_change_passwd=True,
   ...     custom_fields=[{'id': 1, 'value': 'foo'}, {'id': 2, 'value': 'bar'}]
   ... )
   >>> user
   <redminelib.resources.User #1 "John Smith">

Delete methods
--------------

delete
++++++

.. py:method:: delete(resource_id)
   :module: redminelib.managers.ResourceManager
   :noindex:

   Deletes single User resource from Redmine by its id.

   :param int resource_id: (required). User id.
   :return: True

.. code-block:: python

   >>> redmine.user.delete(1)
   True

.. py:method:: delete()
   :module: redminelib.resources.User
   :noindex:

   Deletes current User resource object from Redmine.

   :return: True

.. code-block:: python

   >>> user = redmine.user.get(1)
   >>> user.delete()
   True

Export
------

.. versionadded:: 2.3.0

.. py:method:: export(fmt, savepath=None, filename=None, columns=None, encoding='UTF-8')
   :module: redminelib.resultsets.ResourceSet
   :noindex:

   Exports a resource set of User resources in one of the following formats: csv

   :param string fmt: (required). Format to use for export.
   :param string savepath: (optional). Path where to save the file.
   :param string filename: (optional). Name that will be used for the file.
   :param columns: (optional). Iterable of column names or "all" string for all available columns
    or "all_gui" string for GUI like behaviour or iterable of elements with "all_gui" string and
    additional columns to export.
   :type columns: iterable or string
   :param encoding: (optional). Encoding that will be used for the result file.
   :return: String or Object

.. code-block:: python

   >>> users = redmine.user.all()
   >>> users.export('csv', savepath='/home/jsmith', filename='users.csv', columns='all')
   '/home/jsmith/users.csv'

Editions
========

Standard Edition
----------------

Absolutely free, distributed via PyPI and supports all vanilla Redmine features. Licensed
under Apache 2.0 license. Check the `License <https://python-redmine.com/license.html#standard-edition>`_
for details.

Pro Edition
-----------

Supports additional features like async requests to Redmine, additional Redmine plugins and
so on. Licensed under `Python-Redmine Pro Edition License Version 1.0
<https://python-redmine.com/license.html#pro-edition>`_. License for a Pro Edition can currently only be bought via `TON <https://ton.org>`__ by transferring 25 USDT
to the following wallet address: :code:`UQBn0FIZM1zM7lmIeCczdk9sIMDrvBfFbbuXsYJPdCaFcmYJ`. After the
transaction is complete, be sure to send an email to support@python-redmine.com that contains your transaction ID
and you will receive an email back with all the details regarding Pro Edition installation process. Please give us
at least 3 to 6 hours to process these emails. License doesn't expire and is valid for the current major Python-Redmine
version, e.g. if at the time of purchase current Python-Redmine version is 2.0.1 then license will be valid for
all 2.x.x versions. Below you can find a feature matrix which shows all the differences between these editions:

.. Sphinx and our current theme don't provide a way to create a table in the needed
   format, that is why we are using the raw html with redefined theme stylesheet here.

.. raw:: html

   <table class="feature-matrix">
     <tr>
       <th class="invisible-cell" colspan="1"></th>
       <th class="edition">Standard</th>
       <th class="edition">Pro</th>
     </tr>
     <tr>
       <td class="group" colspan="3">Support (maximum response time)</td>
     </tr>
     <tr>
       <td class="feature">GitHub (no limit)</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Email (24 hours)</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">Engines</td>
     </tr>
     <tr>
       <td class="feature">Sync</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Thread</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Process</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
        <td class="group" colspan="3">Redmine API endpoints</td>
     </tr>
     <tr>
       <td class="feature">Project</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Issue</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">User</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Group</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Role</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Project Membership</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Time Entry</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">News</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Issue Relation</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Version</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Wiki Page</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Query</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">File</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Attachment</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Issue Status</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Issue Category</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Tracker</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Enumeration</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Custom Field</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Search</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">RedmineUP CRM Plugin API endpoints</td>
     </tr>
     <tr>
       <td class="feature">Contact</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Contact Tag</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Note</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Deal</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Deal Status</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Deal Category</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">CRM Query</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">RedmineUP Helpdesk Plugin API endpoints</td>
     </tr>
     <tr>
       <td class="feature">Ticket</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">RedmineUP Checklists Plugin API endpoints</td>
     </tr>
     <tr>
       <td class="feature">Checklist</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">RedmineUP Invoices Plugin API endpoints</td>
     </tr>
     <tr>
       <td class="feature">Invoice</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Invoice Payment</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Expense</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">RedmineUP Products Plugin API endpoints</td>
     </tr>
     <tr>
       <td class="feature">Product</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Product Category</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Order</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Order Status</td>
       <td class="not-implemented">NO</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">Lookups</td>
     </tr>
     <tr>
       <td class="feature">Exact</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">In</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="group" colspan="3">Advanced features</td>
     </tr>
     <tr>
       <td class="feature">Custom Resources</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
     <tr>
       <td class="feature">Authentication Provider</td>
       <td class="implemented">YES</td>
       <td class="implemented">YES</td>
     </tr>
   </table>

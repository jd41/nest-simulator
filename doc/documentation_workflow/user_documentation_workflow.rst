User documentation workflow
###########################

What you need to know
+++++++++++++++++++++

We use `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to generate documentation and `Read the Docs <https://readthedocs.org/>`_ to publish it. Sphinx uses reStructuredText. To learn more about the syntax, check out this `quick reference <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_.

The NEST simulator documentation lives alongside its code. It is contained in the ``doc`` directory within the `NEST source code repository <https://github.com/nest/nest-simulator>`_ on GitHub.

We work with `GitHub <https://www.github.com>`_ as the web-based hosting service for Git. Git allows us to keep our versions under control, with each release of NEST having its own documentation.

.. image:: ../_static/img/documentation_workflow.png
  :width: 500
  :alt: Alternative text


.. note::
   This workflow shows you how to create **user documentation** for NEST. For **developer documentation**, please refer to our :doc:`Developer documentation workflow <developer_documentation_workflow>`.

Changing the documentation
++++++++++++++++++++++++++

If you notice any errors or weaknesses in the documentation, please submit an `issue <https://github.com/nest/nest-simulator/issues>`_ in our GitHub repository.

You can also make changes directly to your forked copy of the `NEST source code repository <https://github.com/nest/nest-simulator>`_ and create a `pull request <https://github.com/nest/nest-simulator/pulls>`_. Just follow the workflow below!

Documentation checklist
+++++++++++++++++++++++
.. To create/add items, I looked through
..   - my own nestdoc_problems file I sent a few months ago, with the stuff that was problematic for me when I learned NEST
..   - cursorily through open and closed documentation PRs, to see what problems occur more often (but I didn't see that much there)
..   - some technical writing/documentation checklists I found on the internet.
..
.. Technical writing checklists online:
..
.. https://medium.com/technical-writing-is-easy/checklists-in-technical-writing-ec732e6b9643 quite short, on level of small texts, seems reasonable (but partially superfluous through Grammarly)
.. https://hmc.tamu.edu/Files/070822TSC%20Writers%20CheckList%20A.pdf very low level, may have been mostly/completely obviated by Grammarly
.. http://techwhirl-1-wpengine.netdna-ssl.com/wp-content/uploads/2014/02/Documentation-Review-Checklist.docx Doc level, not so relevant IMO
.. https://clickhelp.com/clickhelp-technical-writing-blog/using-checklists-in-technical-writing/ short and seemed useful
.. http://www.people.ku.edu/~cmckit/TechComm/TC-Scoring-Checklist.htm rather "grading rubric" than "checklist", quite high-level concepts
.. https://msu.edu/course/be/485/bewritingguideV2.0.pdf very thorough guide and long, not really a checklist
..
.. Book: Atul Gawande: "The Checklist Manifesto", examples of how organizations improved their operations by introducing checklists (e.g. doctors cutting mortality after operations by 1/3 - didn't read it so far, though)

You can save other people - and a later version of yourself - a large multiple of your time investment by writing good documentation. Suboptimal documentation can easily provide negative value by making people commit expensive errors (PR #1772), or just waste time before they ask a human (PR #1740).

When you write or review a documentation pull request, please consider the following suggestion-list. This list is supposed to empower and not smother developers: Decide what to check (and how thoroughly) using your own judgment - but prepare to be judged when you made a mistake after ignoring it.

Documentation level

-does your file belong there in the tree? (e.g. SLI tutorial not in "tutorials" folder)
-Who would want to know about your content, and where in the documentation should it be referenced? (issue #1635, e.g. Running Simulations guide not referenced by Tutorial or anything else AFAIK, so noone from my work group knew its current contents)
-is it redundant? (issue #1634 for some examples and justification)
-if you document some change associated with a string (function name etc.), `grep -r <string> <NEST-SRC>` to see if the documentation needs to be changed somewhere else
-Some pieces of texts are repeated multiple times throughout the documentation. Use `grep -r <string> <NEST-SRC>` to find them if you want to change them all at once
-Compare before and after warnings count during the documentation build process, check that you didn't introduce any new warnings

Titles
-Does the document title make subject+context clear to someone arriving from a search engine? (currently an issue with many titles of tutorials/guides, or SLI/PyNEST stuff not making clear that it refers to SLI/PyNEST)
-Does the document title, vs. those of other documents, allow the reader to clearly distinguish the subject of this file from the subject of all other files? (e.g. MUSIC guide vs MUSIC tutorial: not so clear when one would want to look into what, or "Running Simulations" guide vs NEST tutorial, see also #1634)
-Do all section titles make the subject clear? (not sure about this checklist entry, it may lead to too-verbose titles)
-Appropriate hierarchy of sections and subsections?
-correct TOC (table of contents) tree formatting/tree structure on the left side of the RTD page (e.g. PR #1749, I also saw this problem in some tutorial/guide)

Document level
-What is the related material a reader might want to know about? Is it linked in the document?

Section level
-Is the information complete? (when appropriate - a tutorial should not drown the user in details, but contain links to more thorough reference material) (e.g. I accidentally removed a piece of information in one PR, see https://github.com/nest/nest-simulator/pull/1740#issuecomment-701348226)
-When appropriate, did you document the date of scripts/versions of tools needed etc.?
-Is it concise? Every piece of writing has costs!
-skimmable/split into paragraphs, bullet points when appropriate (e.g. my first attempt at PR #1633?)
-Is related information grouped together?
-Does important information appear first, and/or is the sequence of statements logical?
-What errors could the user make? Are they being warned against clearly and visibly (maybe in several places if appropriate)? In the code, do they cause clear error messages with actionable advice? (PR #1772)

Sentence level
-is the information correct and current?
-Did you try the commands/examples? (as mentioned above, use your own judgment whether this is necessary)
-point of view of users: If I, as a new user, will likely have a question after reading one sentence, is this question answered or acknowledged in the next sentence? (PR #1740)
-unique terms for things (an expert knows that "parameters", "parameter dictionary", "status dictionary" are the same thing, "parameter" is an arbitrary member of the "status dictionary" (rather than e.g. a subset of the members), but "model dictionary" is something else. But using these interchangeably contributes to new user's confusion. Another example: recorder vs detector vs collector). Refer to the list of terms I recently found in the glossary?
-are abbreviations and jargon explained when appropriate?
-Use Grammarly for spell, grammar, and writing checks. The free tier is already useful, the paid tier even better and also makes helpful suggestions regarding readability.

Documentation in the code
-Clear comments on non-obvious things (e.g. comment describing what the Sphinx extensions do, colorize.rst file for PR #1795, the original person who included `.colorize.rst` could have saved me two hours of being wrong and researching when fixing their bug with two minutes of documenting their change themselves). When appropriate, refer to a Pull Request ID.
-Clear error messages (equivalent to entry in "section level")?

Finally
-Did you use this checklist in addition to, rather than as a substitute for, thinking on your own?

-html_search_scorer

TODO cases in point
collector detector recorder parameter status dict param dict model dict
link to https://dangitgit.com/en in NEST development workflow

Setting up your environment
+++++++++++++++++++++++++++

To keep things simple, we have created a conda environment for you. Installing it will enable you to smoothly generate documentation for NEST.

If you are using Linux and want to install a full development environment:

1. Install conda (we recommend `miniconda <https://docs.conda.io/en/latest/miniconda.html#>`_).

2. Switch to the ``doc`` folder in the source directory:

.. code-block:: bash

    cd </path/to/nest_source>/doc

3. Create and activate the environment:

.. code-block:: bash

   conda update -n base -c defaults conda
   conda env create --file nest_doc_conda_env.yml
   conda activate nest-doc

4. If you want to deactivate or delete the build environment:

.. code-block:: bash

   conda deactivate
   conda remove --name nest-doc --all

Generating documentation with Sphinx
++++++++++++++++++++++++++++++++++++

Now that you activated your environment, you can generate HTML files using Sphinx.

Rendering HTML
~~~~~~~~~~~~~~

Using Sphinx, you can build documentation locally and preview it offline:

1. Go to the ``doc`` folder in the source directory:

.. code-block:: bash

    cd </path/to/nest_source>/doc

2. Generate HTML files:

.. code-block:: bash

   make html

3. Preview files. They are then located in ``./_build/html``:

.. code-block:: bash

   cd ./_build/html
   browser filename.html

Editing and creating pages
~~~~~~~~~~~~~~~~~~~~~~~~~~

To edit existing `reStructuredText <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_ files or to create new ones, follow the steps below:

1. You can edit and/or add ``.rst`` files in the ``doc`` directory using your editor of choice.

2. If you create a new page, open ``contents.rst`` in the ``doc`` directory and add the file name under ``.. toctree::``. This will ensure it appears on the NEST simulator documentation's table of contents.

3. If you rename or move a file, please make sure you update all the corresponding cross-references.

4. Save your changes.

5. Re-render documentation as described above.

Previewing on Read the Docs (optional)
++++++++++++++++++++++++++++++++++++++

Proceed as follows to preview your version of the documentation on Read the Docs.

1. Check that unwanted directories are listed in ``.gitignore``:

.. code-block:: bash

   _build
   _static
   _templates

2. Add, commit and push your changes to GitHub.

3. Go to `Read the Docs <https://readthedocs.org/>`_. Sign up for an account if you don't have one.

4. `Import <https://readthedocs.org/dashboard/import/>`_ the project.

5. Enter the details of your project in the ``repo`` field and hit ``Create``.

6. `Build your documentation <https://docs.readthedocs.io/en/stable/intro/import-guide.html#building-your-documentation>`_.

This allows you to preview your work on your Read the Docs account. In order to see the changes on the official NEST simulator documentation, please submit a pull request (see below).

Creating pull request
+++++++++++++++++++++

When you feel your documentation work is finished, you can create a `pull request <https://nest.github.io/nest-simulator/development_workflow#create-a-pull-request>`_ to the ``master`` branch of the NEST Source Code Repository. Your pull request will be reviewed by our NEST Documentation Team!

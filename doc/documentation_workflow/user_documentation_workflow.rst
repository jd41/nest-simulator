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

You can also make changes directly to your forked copy of the `NEST source code repository <https://github.com/nest/nest-simulator>`_ and create a `pull request (PR) <https://github.com/nest/nest-simulator/pulls>`_. Just follow the workflow below!

Documentation suggestion-list
+++++++++++++++++++++++++++++
.. WARNING: If you change the list, you must change the link in the Markdown snippet!
..
..
.. To create/add items to that list, I (@jd41) looked through
..   - my own nestdoc_problems file I sent around a few months ago, with the stuff that was problematic for me when I learned NEST
..   - cursorily through open and closed documentation PRs, to see what problems occur more often (but I didn't see that much there)
..   - some technical writing/documentation checklists I found on the internet.
..
.. Technical writing checklists online:
..
.. https://medium.com/technical-writing-is-easy/checklists-in-technical-writing-ec732e6b9643 relatively short, on level of small texts, seems reasonable (but partially superfluous through Grammarly)
.. https://hmc.tamu.edu/Files/070822TSC%20Writers%20CheckList%20A.pdf low level, may have been mostly/completely obviated by Grammarly
.. http://techwhirl-1-wpengine.netdna-ssl.com/wp-content/uploads/2014/02/Documentation-Review-Checklist.docx Doc level, not so relevant in my opinion
.. https://clickhelp.com/clickhelp-technical-writing-blog/using-checklists-in-technical-writing/ short and seemed useful
.. http://www.people.ku.edu/~cmckit/TechComm/TC-Scoring-Checklist.htm rather "grading rubric" than "checklist", high-level concepts
.. https://msu.edu/course/be/485/bewritingguideV2.0.pdf very thorough guide and long, not really a checklist
..
.. Book: Atul Gawande: "The Checklist Manifesto", examples of how organizations improved their operations by introducing checklists (e.g. doctors cutting mortality after operations by 1/3 - didn't read it so far, though)

You can save other people - and a later version of yourself - a large multiple of your time investment by writing good documentation. Suboptimal documentation can easily provide negative value by making people commit expensive errors (PR - pull request - #1772), or waste time before they ask a human (PR #1740). Feel free to learn more about technical writing on your own.

When you write or review a documentation PR, please consider the following suggestion-list. This list is supposed to empower and not smother developers: Decide what to check (and how thoroughly) using your judgment - but prepare to be judged if you made a mistake after ignoring it. Please document what you checked in the PR discussion in the following style:

.. code-block::

   ### Suggestion-list
   From [this version of the documentation suggestion-list](https://github.com/nest/nest-simulator/blob/88a4e6985dabaad6e93e495e23db9697ce4da46c/doc/documentation_workflow/user_documentation_workflow.rst#documentation-suggestion-list), I checked D1-D3, P1-P3, C2.
   #### Notes:
   D2: Some notes/discussion regarding that checklist item.

.. warning::
   The entries in "Documentation level" and "Titles" should be checked by the NEST documentation team, which has an overview of the complete documentation.

Documentation level
~~~~~~~~~~~~~~~~~~~
**D1. Does your content have a clear purpose that isn't fulfilled by anything that exists elsewhere?**

   - See issue #1634 for some examples and justifications.
   - MUSIC tutorial vs MUSIC guide: The difference in purpose and content is at least not evident on first sight.

**D2. Who else would want to know about your content, and where? Are there appropriate inbound references to your content?**

   - See issue #1635
   - "Running Simulations" guide not referenced by PyNEST tutorial or anything else AFAIK, so no one from a particular user's workgroup knew its current contents.

**D3. Conversely: What is the relevant related material? Are there appropriate outbound references to that material?**

**D4. Is your file in a good position in the documentation tree?**

   - SLI tutorial not in "tutorials" folder

**D5. Did you use Grammarly for spelling, grammar, and writing suggestions?**
   
   - The free tier of `Grammarly <https://www.grammarly.com/>`_ is useful and contains a spell checker.
   - The paid tier is better and makes helpful suggestions regarding style and readability.

**D6. If you document some change associated with a string (function name etc.), did you `grep -r <string> <NEST-SRC>` to see if the documentation needs to be changed somewhere else?**

**D7. Some pieces of texts are repeated multiple times throughout the documentation. If you changed one, did you use `grep -r <string> <NEST-SRC>` to find them all?**

**D8. Did the change introduce new warnings/errors during the documentation build process?**
   
   - Sphinx outputs a count of warnings near the end; compare before/after.
   - Issue #1794 could have been avoided that way.
   - Many current warnings reflect real problems with the rendering output.

**D9. Does the content render correctly, and does the formatting conform to the NEST documentation standards?**

Titles and document structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**T1. Does the document title make subject and context clear to someone arriving from a search engine?**
   
   - Currently an issue with many titles of tutorial/guide sections
   - SLI/PyNEST stuff not making clear that it refers to SLI/PyNEST

**T2. Does the document title allow the reader to clearly distinguish the subject of this file from the subject of any other file?**
   
   - MUSIC guide vs MUSIC tutorial: not immediately clear when one would want to look into what
   - "Running Simulations" guide vs NEST tutorial
   - see also issue #1634

.. not sure about this checklist entry, it may lead to too-verbose titles

**T3. Do all section titles make the subject clear?**

**T4. Consider the arrangement of information. Is it logical? Does important information appear first? Does related information appear close together?**
   
   - These goals are usually contradictory to some extent.

**T5. Appropriate hierarchy of sections and subsections?**

**T6. Correct TOC (table of contents) tree structure on the left side of the RTD page?**
   
   - Current entries when clicking on "Guides" or "Tutorials" on the RTD main page
   - PR #1749

Section level
~~~~~~~~~~~~~
**S1. Is the information as complete as appropriate?**
   
   - A tutorial should not drown the user in details but contain links to more thorough reference material.
   - A proposed change accidentally removed a piece of information in one PR, see `here <https://github.com/nest/nest-simulator/pull/1740#issuecomment-701348226>`_.

**S2. Is the information concise? Every piece of writing has costs!**

**S3. Is the content skimmable and split into paragraphs and bullet points as appropriate?**
   
   - The first attempt at PR #1633

**S4. Point T4 applied within one section.**

**S5. What errors could the user make when applying this documentation? Are they being warned against them clearly and visibly, in several places if appropriate, and using the `.. warning:: role?`**
    
   - PR #1772

Phrase level
~~~~~~~~~~~~
**P1. Imagine being a new user. Will you likely have a question after reading a sentence? Is this question answered or acknowledged in the next sentence?**
   
   - PR #1740

**P2. Did you try the commands/examples?**

**P3. Did you document the versions of tools with which you tried?**

**P4. Do you use the terms in the glossary?**

   - An expert knows that "parameters", "parameter dictionary", "status dictionary" are the same thing, "parameter" is an arbitrary member of the "status dictionary" (rather than a subset of the members), but "model dictionary" is something else. But using these interchangeably contributes to new user's confusion.
   - Another example: recorder vs detector vs collector.

**P5. Are abbreviations and jargon explained when appropriate, linked to the glossary, or both?**

**P6. Is the information correct and up-to-date?**

Documentation in the code
~~~~~~~~~~~~~~~~~~~~~~~~~
**C1. Did you document all non-obvious code with comments? Are the comments clear? Do they refer to an issue/PR number when appropriate?**
   
   - Not clear to a new developer what the Sphinx extensions do and where they are needed because there are no comments in `conf.py``
   - PR #1795: the original person who included `.colorize.rst` could have saved someone two hours of being wrong and researching when fixing their bug with two minutes of writing comments in `.colorize.rst`.

**C2. When you changed the code, did you change all comments and documentation accordingly?**

**C3. Does committing any potential mistake found in S5 cause clear error or warning messages, ideally with actionable and relevant advice?**
   
   - PR #1772

Finally
~~~~~~~
**F1. Did you use this checklist in addition to, rather than as a substitute for, thinking on your own?**

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

This allows you to preview your work on your Read the Docs account. In order to see the changes on the official NEST simulator documentation, please submit a PR (see below).

Creating pull request (PR)
++++++++++++++++++++++++++

When you feel your documentation work is finished, you can create a `PR <https://nest.github.io/nest-simulator/development_workflow#create-a-pull-request>`_ to the ``master`` branch of the NEST Source Code Repository. Your PR will be reviewed by our NEST Documentation Team!

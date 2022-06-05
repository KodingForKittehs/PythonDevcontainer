# PythonDevcontainer
My python devcontainer template and testing area.

## Tips
- The green >< button in the lower left in vscode has the remote containers menus, such as restarting in a container.
- You can add extensions to devcontainer.json from the extension 'Manage' button.

## Troubleshooting
- Ran into errors accessing /tmp/vsch using non-root user, need to revisit.
- Linter flake8 is not installed, click install, get error "There is no Pip installer available in the selected environment"
  ```
    root@ecefb89514c4:/workspaces/PythonDevcontainer# pip --version
    pip 21.2.4 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
    root@ecefb89514c4:/workspaces/PythonDevcontainer# pip3 --version
    pip 21.2.4 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
    root@ecefb89514c4:/workspaces/PythonDevcontainer# python --version
    Python 3.8.12
    root@ecefb89514c4:/workspaces/PythonDevcontainer# python3 --version
    Python 3.8.12
  ```
  If you open the Control Palette (ctrl-shift-p) in vscode and 'Select Interpreter', it shows Python 3.9 is selected and recommended.  Change this to Python 3.8, the prompt to install pyflake reappears and should now work.
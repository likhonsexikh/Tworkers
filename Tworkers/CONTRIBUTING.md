# Contributing to Tworkers

We're excited that you're interested in contributing to Tworkers! Your help is essential for keeping it great.

## Development Setup

1.  **Fork & Clone:** Fork the repository and clone it to your local machine.
2.  **Install Dependencies:** Ensure you have Python and Node.js installed. Run `./setup.sh` to install the core Python dependencies.
3.  **Virtual Environment:** It is highly recommended to use a Python virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Using Xterm.js Beta Builds for Testing

The web interface for Tworkers relies on Xterm.js. If you are testing new features or verifying bug fixes related to the terminal interface, you may need to use their latest beta build.

Our web application uses the CDN version of Xterm.js for simplicity. To test with a beta build, you would typically need to set up a local Node.js environment for the front-end:

1.  Navigate to the `webapp/` directory.
2.  Initialize a `package.json`: `npm init -y`
3.  Install the beta build:
    ```bash
    npm install -S xterm@beta
    ```
4.  You would then need to configure a build tool (like Webpack or Vite) to bundle the local `node_modules` version of Xterm.js instead of using the CDN link in `index.html`.

*For more information on contributing directly to Xterm.js, please see the official [Xterm.js contribution guide](https://github.com/xtermjs/xterm.js/wiki/Contributing).*

## License Agreement for Contributions

If you contribute code to this project, you are implicitly allowing your code to be distributed under the MIT license. You are also implicitly verifying that all code is your original work.

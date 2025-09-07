document.addEventListener('DOMContentLoaded', () => {
    const term = new Terminal({
        cursorBlink: true,
        fontFamily: '"Cascadia Code", "Fira Code", monospace',
        fontSize: 16,
        theme: {
            background: '#0c0c0c',
            foreground: '#00ff41',
            cursor: '#00ff41',
            selectionBackground: '#006400',
        }
    });

    term.open(document.getElementById('terminal'));
    term.focus();

    const socket = io();
    let currentInput = '';
    const promptChar = '$ ';

    const writePrompt = () => term.write(`\r\n${promptChar}`);

    // Display initial welcome message
    term.writeln('  _______ __ __   .__   __.   .__   __. .__    __   __   __  ');
    term.writeln(' |   ____|  |  |  |  \\ |  |   |  \\ |  | |  |  |  | |  | |  | ');
    term.writeln(' |  |__  |  |  |  |   \\|  |   |   \\|  | |  |  |  | |  | |  | ');
    term.writeln(' |   __| |  |  |  |  . `  |   |  . `  | |  |  |  | |  | |  | ');
    term.writeln(' |  |    |  `--`  |  |\\   |   |  |\\   | |  `--`  | |  `--`  | ');
    term.writeln(' |__|     \\______/|__| \\__|   |__| \\__|  \\______/   \\______/  ');
    term.writeln('\r\nWelcome to the Tworkers AI Agent Terminal.');
    term.writeln('Type a command and press Enter. For example:');
    term.writeln("-> create a script named test.sh to echo hello world");

    socket.on('connect', () => {
        writePrompt();
    });

    socket.on('agent_response', (data) => {
        // Replace newlines with carriage return + newline for proper terminal display
        term.write(data.output.replace(/\n/g, '\r\n'));
    });

    term.onKey(({ key, domEvent }) => {
        const printable = !domEvent.altKey && !domEvent.ctrlKey && !domEvent.metaKey;

        if (domEvent.key === 'Enter') {
            if (currentInput.trim().length > 0) {
                socket.emit('user_input', { input: currentInput });
            }
            currentInput = '';
            writePrompt();
        } else if (domEvent.key === 'Backspace') {
            if (currentInput.length > 0) {
                term.write('\b \b'); // Move cursor back, write space, move back again
                currentInput = currentInput.slice(0, -1);
            }
        } else if (printable) {
            currentInput += key;
            term.write(key);
        }
    });
});

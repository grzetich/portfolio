---
layout: default
title: AI Assistant
description: "Ask questions about Ed's professional background, resume, projects, and experience using this AI-powered assistant."
permalink: /chatbot.html
---

<div class="section-container">
    <h2>Portfolio AI Assistant</h2>
    <p class="post-meta">Ask questions about Ed's professional background, projects, and experience</p>
    
    <div class="chatbot-container">
        <div class="chat-messages" id="chatContainer">
            <div class="welcome-message">
                <p><strong>Welcome!</strong> I'm here to help answer questions about Ed Grzetich's professional background. Here are some things you can ask:</p>
                <ul>
                    <li>"What is Ed's experience with AWS?"</li>
                    <li>"Tell me about Ed's Pokémon project"</li>
                    <li>"What help panel component did Ed create?"</li>
                    <li>"What AWS services has Ed documented?"</li>
                    <li>"Do you know Microsoft Word?"</li>
                </ul>
            </div>
        </div>
        
        <div class="typing-indicator" id="typingIndicator">
            <span class="typing-dots">Assistant is typing</span>
        </div>
        
        <div class="chat-input-container">
            <input type="text" id="messageInput" placeholder="Ask about Ed's resume, projects, or experience..." />
            <button id="sendButton">Send</button>
        </div>
    </div>
</div>

<style>
/* Chatbot-specific styles that extend the site's design system */
.chatbot-container {
    background: var(--card-background);
    border: 1px solid var(--border-color);
    border-radius: 0.75rem;
    overflow: hidden;
    margin-top: 1.5rem;
}

.chat-messages {
    height: 500px;
    overflow-y: auto;
    padding: 1.5rem;
    background: #f8f9fa;
}

.welcome-message {
    text-align: center;
    color: var(--text-color-secondary);
    padding: 2rem 1rem;
    font-style: italic;
}

.welcome-message ul {
    text-align: left;
    max-width: 400px;
    margin: 1rem auto 0;
}

.welcome-message li {
    margin-bottom: 0.5rem;
    font-style: normal;
    color: var(--brand-color);
}

.message {
    margin-bottom: 1rem;
    max-width: 80%;
    clear: both;
}

.user-message {
    float: right;
    background: var(--brand-color);
    color: white;
    padding: 0.75rem 1rem;
    border-radius: 1.125rem 1.125rem 0.25rem 1.125rem;
    font-size: 0.9rem;
}

.bot-message {
    float: left;
    background: var(--card-background);
    border: 1px solid var(--border-color);
    padding: 1rem;
    border-radius: 0.25rem 1.125rem 1.125rem 1.125rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    position: relative;
}

.bot-message-content {
    margin-bottom: 0.5rem;
    line-height: 1.6;
    color: var(--text-color-primary);
}

.bot-message-content p {
    margin-bottom: 1rem;
}

.bot-message-content p:last-child {
    margin-bottom: 0;
}

.copy-button {
    position: absolute;
    top: 0.75rem;
    right: 0.75rem;
    background: var(--background-color);
    border: 1px solid var(--border-color);
    border-radius: 0.25rem;
    padding: 0.25rem 0.5rem;
    font-size: 0.75rem;
    cursor: pointer;
    color: var(--text-color-secondary);
    transition: all 0.2s;
}

.copy-button:hover {
    background: var(--border-color);
    color: var(--text-color-primary);
}

.copy-button:active {
    background: var(--brand-color);
    color: white;
}

.copy-button.copied {
    background: #22c55e;
    color: white;
    border-color: #22c55e;
}

.typing-indicator {
    padding: 0.75rem 1rem;
    background: var(--card-background);
    border: 1px solid var(--border-color);
    border-radius: 0.25rem 1.125rem 1.125rem 1.125rem;
    margin: 0 1.5rem 1rem;
    max-width: 80%;
    display: none;
}

.typing-dots {
    display: inline-block;
    color: var(--text-color-secondary);
}

.typing-dots::after {
    content: '';
    animation: typing 1.5s infinite;
}

@keyframes typing {
    0%, 60%, 100% { content: ''; }
    30% { content: '.'; }
    60% { content: '..'; }
    90% { content: '...'; }
}

.chat-input-container {
    padding: 1.5rem;
    border-top: 1px solid var(--border-color);
    display: flex;
    gap: 0.75rem;
    background: var(--card-background);
}

#messageInput {
    flex: 1;
    padding: 0.75rem 1rem;
    border: 1px solid var(--border-color);
    border-radius: 1.5rem;
    outline: none;
    font-size: 0.9rem;
    background: var(--background-color);
    color: var(--text-color-primary);
}

#messageInput:focus {
    border-color: var(--brand-color);
    box-shadow: 0 0 0 2px rgba(185, 28, 28, 0.1);
}

#sendButton {
    background: var(--brand-color);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 1.5rem;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: background 0.2s;
}

#sendButton:hover:not(:disabled) {
    background: var(--brand-color-dark);
}

#sendButton:disabled {
    background: #9ca3af;
    cursor: not-allowed;
}

.error-message {
    background: #fef2f2;
    color: #991b1b;
    border: 1px solid #fecaca;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    float: left;
    max-width: 80%;
    clear: both;
}

/* Clear floats after messages */
.chat-messages::after {
    content: "";
    display: table;
    clear: both;
}
</style>

<script>
const API_BASE_URL = 'http://localhost:8000'; // Change this to your deployed API URL

const chatContainer = document.getElementById('chatContainer');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const typingIndicator = document.getElementById('typingIndicator');

let isFirstMessage = true;

function formatResponseText(text) {
    // Clean up the text and split into logical paragraphs
    let formattedText = text
        .replace(/\n/g, ' ') // Replace single newlines with spaces
        .replace(/\s+/g, ' ') // Normalize whitespace
        .trim();
    
    // Split by common paragraph indicators
    const paragraphs = formattedText
        .split(/(?:\.|!|\?)\s+(?=[A-Z]|•|\*|For\s|The\s|This\s|Ed\s|His\s|In\s|Additionally|Furthermore|Moreover|However|While)/g)
        .filter(p => p.trim().length > 0)
        .map(p => {
            let paragraph = p.trim();
            // Add period back if it was removed and doesn't already end with punctuation
            if (!paragraph.match(/[.!?]$/)) {
                paragraph += '.';
            }
            return `<p>${paragraph}</p>`;
        });
    
    // If we couldn't split effectively, just return the original text in paragraphs
    if (paragraphs.length <= 1) {
        // Try splitting on sentence boundaries for long text
        const sentences = formattedText.split(/(?<=[.!?])\s+/);
        if (sentences.length > 3) {
            const midpoint = Math.ceil(sentences.length / 2);
            const firstHalf = sentences.slice(0, midpoint).join(' ');
            const secondHalf = sentences.slice(midpoint).join(' ');
            return `<p>${firstHalf}</p><p>${secondHalf}</p>`;
        } else {
            return `<p>${formattedText}</p>`;
        }
    }
    
    return paragraphs.join('');
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        // Success - handled by button state change
    }).catch(function(err) {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
    });
}

function addMessage(content, isUser = false, isError = false) {
    if (isFirstMessage) {
        chatContainer.innerHTML = '';
        isFirstMessage = false;
    }

    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : isError ? 'error-message' : 'bot-message'}`;
    
    if (isUser || isError) {
        messageDiv.innerHTML = content;
    } else {
        // Format bot messages with paragraphs and copy button
        const formattedContent = formatResponseText(content);
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'bot-message-content';
        contentDiv.innerHTML = formattedContent;
        
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.innerHTML = '📋 Copy';
        copyButton.addEventListener('click', () => copyResponse(copyButton, content));
        
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(copyButton);
    }
    
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function copyResponse(button, text) {
    copyToClipboard(text);
    const originalText = button.innerHTML;
    button.innerHTML = '✅ Copied!';
    button.classList.add('copied');
    
    setTimeout(() => {
        button.innerHTML = originalText;
        button.classList.remove('copied');
    }, 2000);
}

function showTyping() {
    typingIndicator.style.display = 'block';
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function hideTyping() {
    typingIndicator.style.display = 'none';
}

async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;

    // Add user message
    addMessage(message, true);
    messageInput.value = '';
    sendButton.disabled = true;
    showTyping();

    try {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        hideTyping();
        addMessage(data.response);
        
    } catch (error) {
        hideTyping();
        addMessage(`Error: Unable to get response. ${error.message}`, false, true);
    } finally {
        sendButton.disabled = false;
        messageInput.focus();
    }
}

sendButton.addEventListener('click', sendMessage);

messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Focus on input when page loads
messageInput.focus();
</script>
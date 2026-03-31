const fetch = require('node-fetch');

async function getData() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        
        console.log("Статус код:", response.status);
        
        const data = await response.json();
        console.log("Данні від сервера:", data);
    } catch (error) {
        console.error("Помилка:", error);
    }
}

getData();
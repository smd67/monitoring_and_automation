<!-- DataTable.vue -->
  <template>
    <div class="my-division">
        <button class="my-button" @click="triggerOperationA">Operation A</button>
        <button class="my-button" @click="triggerOperationB">Operation B</button>
        <button class="my-button" @click="triggerOperationC">Operation C</button>
        <button class="my-button" @click="triggerOperationD">Operation D</button>
        <button class="my-button" @click="triggerOperationE">Operation E</button>
        <button class="my-button" @click="triggerOperationF">Operation F</button>
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    data() {
      return {};
    },
    methods: {
      handleData(data) {
        this.url = data;
      },
      async triggerOperationA() {
        const apiUrl = 'http://127.0.0.1:8002/operation-a/'; // Replace with your actual API endpoint
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
          const response = await axios.get(apiUrl, config);
        } catch (error) {
          console.error('Error fetching data:', error);
        } 
      },
      async triggerOperationB() {
        const apiUrl = 'http://127.0.0.1:8002/operation-b/'; // Replace with your actual API endpoint
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
          const response = await axios.get(apiUrl, config);
        } catch (error) {
          console.error('Error fetching data:', error);
        } 
      },
      async triggerOperationC() {
        const apiUrl = 'http://127.0.0.1:8002/operation-c/'; // Replace with your actual API endpoint
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
          const response = await axios.get(apiUrl, config);
        } catch (error) {
          console.error('Error fetching data:', error);
        } 
      },
      async triggerOperationD() {
        const apiUrl = 'http://127.0.0.1:8002/operation-d/'; // Replace with your actual API endpoint
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
          const response = await axios.get(apiUrl, config);
        } catch (error) {
          console.error('Error fetching data:', error);
        } 
      },
      async triggerOperationE() {
        const apiUrl = 'http://127.0.0.1:8002/operation-e/'; // Replace with your actual API endpoint
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
          const response = await axios.get(apiUrl, config);
        } catch (error) {
          console.error('Error fetching data:', error);
        } 
      },
      async triggerOperationF() {
        const apiUrl = 'http://127.0.0.1:8002/operation-f/'; // Replace with your actual API endpoint
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        try {
          const response = await axios.get(apiUrl, config);
        } catch (error) {
          console.error('Error fetching data:', error);
        } 
      },
    },
  };
  </script>

  <style scoped>
  /* Add basic styling for the table if needed */
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  th {
    background-color: #f2f2f2;
  }
  .my-division {
    padding-top: 82px;
    padding-bottom: 30px;
  }
  .spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #3498db;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  .grid-container {
    display: grid;
    grid-template-columns: repeat(5, 1fr); /* 5 columns, equal width */
    grid-template-rows: repeat(1, auto); /* 1 rows, height determined by content */
    gap: 1px; /* Adjust as needed for spacing */
  }
  .grid-item {  
    /* Optional: Add styling for individual grid items */
    display: inline-block;
    border: 1px solid #ccc;
    padding: 1px;
  }
  </style>
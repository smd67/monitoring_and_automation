<template>
  <div>
    <input type="text" 
      v-model="inputText" 
      @focus="showDropdown = true"
      @input="filterOptions"
      @click="showDropdown = true"
      @blur="hideDropdown"
      placeholder="Type to search..."
      class="my-input" 
    />
    <button class="my-button" @click="triggerAction">Save</button>
    <div class="dropdown-menu">
      <ul v-if="showDropdown">
        <li v-for="option in filteredOptions" :key="option.value" @click="selectOption(option)">
          {{ option.text }}
        </li>
      </ul>
    </div>
  </div>
  
</template>

<script>
  export default {
    data() {
      return {
        inputText: '',
        options: [],
        filteredOptions: [],
        showDropdown: false
      };
    },
    async created() {
      try {
        const response = await fetch('http://127.0.0.1:8001/get-palette-groups/');
        this.options = await response.json();
      } catch (error) {
        console.error("Error fetching data:", error);
      }
      this.filteredOptions = this.filterOptions();
    },
    
    methods: {
      filterOptions() {
        return  this.options;
      },
      triggerAction() {
        console.log("in triggerAction")
        this.$emit('download-data');
      },
      selectOption(option) {
        this.inputValue = option.value;
        this.inputText = option.text;
        this.$emit('data-sent', this.inputValue);
        this.$emit('button-clicked'); // Emit a custom event
        this.showDropdown = false;
      },
      hideDropdown() {
        // Use a timeout to allow click event on list items to register
        setTimeout(() => {
          this.showDropdown = false;
        }, 150);
      }
    }
  }
</script>

<style scoped>
.my-button {
  margin-right: 5px;
  height: 30px;
  min-width: 40px;
  width: 10%;
}
.my-input {
  height: 30px;
  width: 85%;
  cursor: pointer;
}

/* Targeting all ul elements within the component */
ul {
  list-style-type: none;
}

.dropdown-menu {
  max-height: 150px; /* Adjust as needed */
  overflow-y: auto;
  border: 1px solid #ccc;
  list-style: none;
  padding: 0;
  margin: 0;
  list-style-type: none;
  border-top: none;
  width: 85%;
}

.dropdown-menu li {
  padding: 8px 12px;
  cursor: pointer;
}

.dropdown-menu li:hover {
  background-color: #f0f0f0;
}
</style>
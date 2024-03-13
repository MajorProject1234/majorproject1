function generateQuery() {
    const conditions = document.getElementById('queryTextArea').value;
    
    const generatedQuery = `SELECT * FROM your_table WHERE ${conditions};`;
  
    document.getElementById('generatedQuery').innerText = generatedQuery;
  }
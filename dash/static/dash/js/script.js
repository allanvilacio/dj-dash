const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
const headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
};


function updateURLs(formId) {
    const filtros = document.querySelectorAll(`#${formId} input, textarea`);
    const values = {};
    
    filtros.forEach(i =>{
        values[i.name]=i.value
    })
    const queryParams = new URLSearchParams(values).toString();
    window.history.pushState({}, '', `?${queryParams}`);
    filterGraphs() 
}

function createGraph(idsDiv, path){
    data_ini = document.getElementById('data_ini').value;
    data_fim = document.getElementById('data_fim').value;
    fetch(`${path}`, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify({ data_ini: data_ini, data_fim: data_fim })
    })
    .then(response => response.json())
    .then(data =>{
        const plotData = JSON.parse(data);
        for(let i=0; i<idsDiv.length; i++){
            Plotly.newPlot(idsDiv[i], plotData[i]);
        }
    })
}

function updateAllGraphs(){
    createGraph(['graph1', 'graph2'], '/graph')
}
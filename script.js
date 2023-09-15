const node_size = 20;

const nodesData = [
    { id: 'USD', size: node_size, text: 'USD' },
    { id: 'EUR', size: node_size, text: 'EUR' },
    { id: 'GBP', size: node_size, text: 'GBP' },
    { id: 'CNY', size: node_size, text: 'CNY' },
    { id: 'JPY', size: node_size, text: 'JPY' },
    { id: 'AUD', size: node_size, text: 'AUD' },
    { id: 'CAD', size: node_size, text: 'CAD' },
    { id: 'CHF', size: node_size, text: 'CHF' },
    { id: 'SGD', size: node_size, text: 'SGD' },
    { id: 'HKD', size: node_size, text: 'HKD' }
];

const links = [];
for (let i = 0; i < nodesData.length; i++) {
    for (let j = i + 1; j < nodesData.length; j++) {
        links.push({ source: nodesData[i].id, target: nodesData[j].id });
    }
}




console.log("YO")
// const fs = require('fs');
// const path = require('path');
// 
// const ratesData = JSON.parse(fs.readFileSync(path.join(__dirname, 'data', 'rates.json')));
// const links = [];
// 
// nodesData.forEach(node1 => nodesData.forEach(node2 => {
//   if (node1.id !== node2.id && ratesData[node1.id] && ratesData[node1.id][node2.id]) {
//     links.push({ source: node1.id, target: node2.id, value: ratesData[node1.id][node2.id] });
//   }
// }));
// 
// console.log(links);






const svg = d3.select("#graph-container")
    .append("svg")
    .attr("width", "100%")
    .attr("height", "100%");

const simulation = d3.forceSimulation(nodesData)
    .force("link", d3.forceLink().id(d => d.id).distance(500))
    .force("charge", d3.forceManyBody().strength(-30))
    .force("center", d3.forceCenter(svg.node().getBoundingClientRect().width / 2, svg.node().getBoundingClientRect().height / 2))
    .on("tick", ticked);

function ticked() {
    link.attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node.attr("cx", d => d.x)
        .attr("cy", d => d.y);

    nodeText.attr("x", d => d.x)
        .attr("y", d => d.y);
}

simulation.nodes(nodesData);
simulation.force("link").links(links);
simulation.alpha(1).restart();

const link = svg.selectAll(".link")
    .data(links)
    .enter()
    .append("line")
    .attr("class", "link")
    .on("mouseover", function (event, d) {
        d3.select(this)
            .attr("stroke", "red");
        svg.append("text")
            .attr("class", "edge-label")
            .attr("x", (d.source.x + d.target.x) / 2)
            .attr("y", (d.source.y + d.target.y) / 2)
            .text(`${d.source.id} -> ${d.target.id}`);
    })
    .on("mouseout", function (event, d) {
        d3.select(this)
            .attr("stroke", "#ccc");
        svg.selectAll(".edge-label").remove();
    });

const node = svg.selectAll(".node")
    .data(nodesData)
    .enter()
    .append("circle")
    .attr("class", "node")
    .attr("r", d => d.size)
    .call(d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended));

const nodeText = svg.selectAll(".node-text")
    .data(nodesData)
    .enter()
    .append("text")
    .attr("class", "node-text")
    .attr("dy", 5)
    .text(d => d.text);

function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

const centerForceInput = document.getElementById("centerForce");
const centerForceValue = document.getElementById("centerForceValue");
const repelForceInput = document.getElementById("repelForce");
const repelForceValue = document.getElementById("repelForceValue");
const linkDistanceInput = document.getElementById("linkDistance");
const linkDistanceValue = document.getElementById("linkDistanceValue");

let centerForceStrength = 0.05;
let repelForceStrength = 30;
let linkDistance = 500;

centerForceInput.addEventListener("input", function () {
    centerForceStrength = parseFloat(centerForceInput.value);
    centerForceValue.textContent = centerForceStrength;
    updateForces();
});

repelForceInput.addEventListener("input", function () {
    repelForceStrength = parseInt(repelForceInput.value);
    repelForceValue.textContent = repelForceStrength;
    updateForces();
});

linkDistanceInput.value = linkDistance;
linkDistanceValue.textContent = linkDistance;

linkDistanceInput.addEventListener("input", function () {
    linkDistance = parseInt(linkDistanceInput.value);
    linkDistanceValue.textContent = linkDistance;
    updateForces();
});

function updateForces() {
    simulation.force("center", d3.forceCenter(svg.node().getBoundingClientRect().width / 2, svg.node().getBoundingClientRect().height / 2).strength(centerForceStrength));
    simulation.force("charge", d3.forceManyBody().strength(-repelForceStrength));
    simulation.force("link", d3.forceLink(links).id(d => d.id).distance(linkDistance));
    simulation.alpha(1).restart();
}

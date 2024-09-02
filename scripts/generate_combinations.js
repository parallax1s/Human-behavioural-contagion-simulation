const fs = require('fs');
const path = require('path');

const imagesDir = path.join(__dirname, '../docs/images');
const outputFilePath = path.join(__dirname, '../docs/combinations.json');

const combinations = {};

fs.readdirSync(imagesDir).forEach(folder => {
    const match = folder.match(/agents_(\d+)_dens_(\d+\.\d+)/);
    if (match) {
        const agents = match[1];
        const density = match[2];
        if (!combinations[agents]) {
            combinations[agents] = [];
        }
        combinations[agents].push(density);
    }
});

fs.writeFileSync(outputFilePath, JSON.stringify(combinations, null, 2));

console.log('Combinations file generated:', outputFilePath);

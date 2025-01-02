function makeButton(pattern, uuids) {
  button = document.createElement("span");
  button.textContent = fixButtonText(pattern);

  button.addEventListener("pointerup", function (event) {
    navigator.bluetooth
      .requestDevice({
        filters: [
          {
            services: [uuids.service],
          },
        ],
      })
      .then((device) => {
        console.log(device.name);
        return device.gatt.connect();
      })
      .then((server) => server.getPrimaryService(uuids.service))
      .then((service) => service.getCharacteristic(uuids.pattern))
      .then((characteristic) => {
        return sendPattern(characteristic, pattern);
      })
      .catch((error) => {
        console.error(error);
      });
  });

  return button;
}

function sendPattern(characteristic, pattern) {
    console.log(pattern);
    characteristic.writeValue(new TextEncoder().encode(pattern))
}

function populateButtons(buttons, data) {
  data.patterns.forEach((pattern) => {
    buttons.appendChild(makeButton(pattern, data.uuids));
  });
}

function fixButtonText(text) {
  return text.split("_").join(" ");
}

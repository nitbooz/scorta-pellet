"""
Custom Lovelace card for pellet stock management.
"""
class PelletCard extends HTMLElement {
    setConfig(config) {
        this._config = config;
    }

    set hass(hass) {
        this._hass = hass;
        this._updateContent();
    }

    _updateContent() {
        if (!this.content) {
            this.innerHTML = `
                <style>
                    .pellet-card {
                        padding: 16px;
                        text-align: center;
                    }
                    .pellet-button {
                        background: none;
                        border: none;
                        cursor: pointer;
                    }
                    .pellet-icon {
                        font-size: 48px;
                    }
                    .pellet-count {
                        font-size: 24px;
                        margin-top: 8px;
                    }
                </style>
                <div class="pellet-card">
                    <button class="pellet-button" id="pellet-btn">
                        <ha-icon icon="mdi:sack" class="pellet-icon"></ha-icon>
                    </button>
                    <div class="pellet-count" id="pellet-count">0 sacchi</div>
                </div>
            `;
            this.content = true;
            
            this.querySelector('#pellet-btn').addEventListener('click', () => {
                const quantity = prompt('Quanti sacchi vuoi scalare dalla scorta?');
                if (quantity) {
                    this._hass.callService('scorta_pellet', 'remove_pellet', {
                        quantity: parseInt(quantity)
                    });
                }
            });
        }
        
        const state = this._hass.states['sensor.scorta_pellet'];
        if (state) {
            this.querySelector('#pellet-count').innerText = `${state.state} sacchi`;
        }
    }
}

customElements.define('pellet-card', PelletCard);
package plugins

type Plugin struct {
	Name   string
	active bool
}

func New(name string) *Plugin {
	return &Plugin{Name: name, active: false}
}

// changes the status to true
func (p *Plugin) Start() {
	p.active = true
}

// get the status from a private struct
func (p *Plugin) IsActive() bool {
	return p.active
}

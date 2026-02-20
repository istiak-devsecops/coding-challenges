package monitor

type Service struct {
	Name     string
	isOnline bool
}

func NewService(name string, online bool) *Service {
	return &Service{
		Name:     name,
		isOnline: online,
	}
}

func (s *Service) Status() bool {
	return s.isOnline
}

func (s *Service) Toggle() {
	if s.Name == "" {
		return
	}
	s.isOnline = !s.isOnline
}

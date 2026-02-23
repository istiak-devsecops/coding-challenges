package registry

import "sync"

// === Store Struct ===
type Store struct {
	mu   sync.RWMutex
	data map[string]string
}

// === Store Constructor ===
func NewStore() *Store {
	return &Store{
		data: make(map[string]string),
	}
}

// === Save Method ===
func (s *Store) Save(name, status string) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.data[name] = status
}

// === List Method ===
func (s *Store) List() map[string]string {
	s.mu.RLock()
	defer s.mu.RUnlock()

	result := make(map[string]string, len(s.data))
	for k, v := range s.data {
		result[k] = v
	}
	return result
}

// === Get Method ===
func (s *Store) Get(name string) (string, bool) {
	val, exist := s.data[name]
	return val, exist
}

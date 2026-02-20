package logger

import "fmt"

// Processor Interface
type Processor interface {
	Process() string
}

// The data stracture
type Entry struct {
	Source  string
	Message string
}

// Security log stracture
type SecurityLog struct{ Entry }

func NewSecurityLog(source, msg string) *SecurityLog {
	return &SecurityLog{Entry: Entry{Source: source, Message: msg}}
}

func (s *SecurityLog) Process() string {
	return fmt.Sprintf("Source: %s | Message: %s\n", s.Source, s.Message)
}

// Build log stracture
type BuildLog struct{ Entry }

func NewBuildLog(source, msg string) *BuildLog {
	return &BuildLog{Entry: Entry{Source: source, Message: msg}}
}

func (s *BuildLog) Process() string {
	return fmt.Sprintf("Source: %s | Message: %s\n", s.Source, s.Message)
}

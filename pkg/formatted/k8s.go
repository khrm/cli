package formatted

import (
	"github.com/knative/pkg/apis"
	corev1 "k8s.io/api/core/v1"
)

// Condition returns a human readable text based on the status of the Condition
func Condition(c []apis.Condition) string {

	var status string
	if len(c) == 0 {
		return "---"
	}

	switch c[0].Status {
	case corev1.ConditionFalse:
		status = "Failed"
	case corev1.ConditionTrue:
		status = "Succeeded"
	case corev1.ConditionUnknown:
		status = "Running"
	}

	if c[0].Reason != "" && c[0].Reason != status {
		status = status + "(" + c[0].Reason + ")"
	}

	return status
}

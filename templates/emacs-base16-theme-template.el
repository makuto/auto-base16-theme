;;
;; Custom theme
;;

(require 'base16-theme)

(defvar base16-my-auto-colors
  '(:base00 "#{}"
    :base01 "#{}"
    :base02 "#{}"
    :base03 "#{}"
    :base04 "#{}"
    :base05 "#{}"
    :base06 "#{}"
    :base07 "#{}"
    :base08 "#{}"
    :base09 "#{}"
    :base0A "#{}"
    :base0B "#{}"
    :base0C "#{}"
    :base0D "#{}"
    :base0E "#{}"
    :base0F "#{}")
  "All colors for Base16 Macoy are defined here.")

;; Define the theme
(deftheme base16-my-auto)

;; Add all the faces to the theme
(base16-theme-define 'base16-my-auto base16-my-auto-colors)

;; Mark the theme as provided
(provide-theme 'base16-my-auto)

(provide 'base16-my-auto-theme)

;;; base16-my-auto-theme.el ends here
